import re
from aiohttp import ClientSession
from sqlalchemy import insert

from app.database.base import session_factory
from app.database.dbmodels import Currencies


api_url = "https://test.deribit.com/api/v2"

btc_payload = {
    "jsonrpc": "2.0",
    "id": 8066,
    "method": "public/ticker",
    "params": {
        "instrument_name": "BTC-PERPETUAL"
    }
}

eth_payload = {
    "jsonrpc": "2.0",
    "id": 8066,
    "method": "public/ticker",
    "params": {
        "instrument_name": "ETH-PERPETUAL"
    }
}

async def get_response_result(result: dict) -> tuple:
    price = result['result']['index_price']
    ticker = result['result']['instrument_name']
    ticker = re.match(r'^(.*?)-PERPETUAL$', ticker).group(1)
    print(ticker)
    return (ticker, price)

async def write_into_db(ticker: str, usd_price: float):
    async with session_factory() as db_session:
        stmt = insert(Currencies).values({"ticker": ticker, "price": usd_price})
        await db_session.execute(stmt)
        await db_session.commit()

async def deribit_request(api_url: str, json_payload: dict) -> tuple | None:
    async with ClientSession() as session:
        async with session.post(url=api_url, json=json_payload) as response:
            if response.status == 200:
                result = await response.json()
                ticker, price = await get_response_result(result=result)
                await write_into_db(ticker=ticker, usd_price=price)
                return (ticker, price)
            else:
                return None

async def get_btc_price() -> dict:
    return await deribit_request(api_url=api_url, json_payload=btc_payload)

async def get_eth_price() -> dict:
    return await deribit_request(api_url=api_url, json_payload=eth_payload)
