from pydantic import BaseModel


class StatisticsByMarketResponse(BaseModel):
    average: float
    median: float
    minimum: int
    maximum: int