from datetime import datetime
from app.utils.CurrenciesRepository import CurrenciesSQLRepository


class CurrenciesService:

    def __init__(self, repository: CurrenciesSQLRepository):
        self.repository = repository()

    async def get_currency_story(self, ticker: str) -> list:
        res = await self.repository.get_currency_story(ticker=ticker)
        if res == []:
            return None
        return res

    async def get_last_currency_price(self, ticker: str):
        res = await self.repository.get_last_currency_price(ticker=ticker)
        return res

    async def get_currency_prices_for_period(self, ticker: str, start: datetime, end: datetime) -> list:
        if end < start:
            return None
        res = await self.repository.get_currency_prices_for_period(ticker=ticker, start=start, end=end)
        if res == []:
            return None
        return res
