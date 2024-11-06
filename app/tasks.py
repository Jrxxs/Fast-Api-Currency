import asyncio
from .celery_conf import celery_app
from .services.api_requests import get_btc_price, get_eth_price


async def get_currencies():
    res_btc = await get_btc_price()
    res_eth = await get_eth_price()

@celery_app.task
def currencies_api_request_task():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_currencies())
