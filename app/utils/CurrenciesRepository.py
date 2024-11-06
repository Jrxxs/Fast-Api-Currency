from datetime import datetime
from sqlalchemy import and_, select

from app.database.dbmodels import Currencies
from app.database.base import session_factory


class CurrenciesSQLRepository:

    async def get_currency_story(self, ticker: str) -> list:
        async with session_factory() as session:
            stmt = select(Currencies).filter_by(ticker=ticker)
            res = await session.execute(stmt)
            res = res.scalars().all()
            return res
        
    async def get_last_currency_price(self, ticker: str):
        """
            SELECT * FROM public.currencies
            WHERE ticker = {ticker}
            ORDER BY gained_at DESC LIMIT 1
        """
        async with session_factory() as session:
            stmt = (
                select(Currencies)
                .filter_by(ticker=ticker)
                .order_by(Currencies.gained_at.desc())
                .limit(1)
            )
            res = await session.execute(stmt)
            res = res.scalars().one_or_none()
            return res

    async def get_currency_prices_for_period(self, ticker: str, start: datetime, end: datetime) -> list:
        """
            SELECT * FROM public.currencies
            WHERE ticker = {ticker}
            AND gained_at BETWEEN {start} AND {end}
        """
        async with session_factory() as session:
            stmt = (
                select(Currencies)
                .filter(and_(Currencies.ticker==ticker, Currencies.gained_at.between(start, end)))
            )
            res = await session.execute(stmt)
            res = res.scalars().all()
            return res