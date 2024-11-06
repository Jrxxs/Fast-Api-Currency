from app.services.CurrenciesService import CurrenciesService
from app.utils.CurrenciesRepository import CurrenciesSQLRepository


async def currencies_service():
    return CurrenciesService(CurrenciesSQLRepository)
