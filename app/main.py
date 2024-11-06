import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import aiohttp
import asyncio
from fastapi import FastAPI
from sqlalchemy import insert

from app.services.api_requests import get_btc_price, get_eth_price
from app.database.queries.orm import create_tables, drop_tables
from app.database.dbmodels import Currencies
from app.database.base import session_factory
from app.tasks import currencies_api_request_task
from app.routes import currencies_router


app = FastAPI()

app.include_router(currencies_router)

async def test_query():
    async with aiohttp.ClientSession() as session:
        btc_usd = await get_btc_price(session)

        eth_usd = await get_eth_price(session)

        print(btc_usd, eth_usd)

async def init_db_test():
    async with session_factory() as session:
        stmt = insert(Currencies).values([
                {"ticker": "BTC", "price": 6863.3},
                {"ticker": "BTC", "price": 6859.8},
                {"ticker": "BTC", "price": 6887.0},
                {"ticker": "ETC", "price": 2856.7}
            ])
        await session.execute(stmt)
        await session.commit()

async def test_celery():
    task = currencies_api_request_task.delay()
    print("world")

async def main():
    
    # await test_query()
    # await test_celery()
    await create_tables()
    # await init_db_test()


if __name__ == '__main__':
    asyncio.run(main())
