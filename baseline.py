#baseline.py
from pydantic import BaseModel

class DataForm(BaseModel):
    tickers : str
    periods: str
    intervals : str