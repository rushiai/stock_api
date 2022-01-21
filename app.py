from fastapi import FastAPI
from baseline import DataForm
import yfinance as yf

app = FastAPI()

@app.get("/")
async def root():
    return {"Welcome this is yahoo finance API by rushidarge goto==>": "url/docs"}


@app.post('/data')
def get_data(data:DataForm):
    data = data.dict()
    df = yf.download(tickers=data['ticker'], period=data['periods'], interval=data['intervals'], \
                     progress=False, show_errors=False, threads=False)
    return df.to_json()

# uvicorn app:app