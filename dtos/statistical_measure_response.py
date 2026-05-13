from pydantic import BaseModel


class StatisticalMeasuresResponse(BaseModel):
    average: float
    median: float
    minimum: int
    maximum: int