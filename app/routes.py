from datetime import date, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from app.utils.dependencies import currencies_service
from app.services.CurrenciesService import CurrenciesService


currencies_router = APIRouter()

@currencies_router.get("/story")
async def get_story(
        ticker: str,
        service: Annotated[CurrenciesService, Depends(currencies_service)]
    ):
    res = await service.get_currency_story(ticker=ticker)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wrong ticker!"
        )
    return res

@currencies_router.get("/last-price")
async def get_last_price(
        ticker: str,
        service: Annotated[CurrenciesService, Depends(currencies_service)]
    ):
    res = await service.get_last_currency_price(ticker=ticker)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wrong ticker!"
        )
    return res

@currencies_router.get("/period")
async def get_period_price(
        ticker: str,
        start: datetime,
        end: datetime,
        service: Annotated[CurrenciesService, Depends(currencies_service)]
    ):
    res = await service.get_currency_prices_for_period(ticker=ticker, start=start, end=end)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wrong ticker or time interval!"
        )
    return res
