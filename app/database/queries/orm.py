from datetime import date, datetime
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../..'))

import asyncio
from sqlalchemy import and_, select
from app.database.base import Base, engine, session_factory
from app.database.dbmodels import Currencies


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# if __name__ == '__main__':
#     res = asyncio.run(get_last_currency_price("ETH-PERPETUAL"))
#     print(res)
