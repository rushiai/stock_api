#baseline.py
from pydantic import BaseModel

class DataForm(BaseModel):
    ticker : str
    periods: str
    intervals : str
