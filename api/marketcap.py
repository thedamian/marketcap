#import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import yfinance as yf

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./templates")

stocks = [
        {"stock": "AAPL", "marketcap": 0},
        {"stock": "NVDA", "marketcap": 0},
        {"stock": "MSFT", "marketcap": 0},
        {"stock": "AMZN", "marketcap": 0},
        {"stock": "GOOGL", "marketcap": 0},
        {"stock": "META", "marketcap": 0},
        {"stock": "TSLA", "marketcap": 0},
        {"stock": "TSM", "marketcap": 0},
        {"stock": "BRK-B", "marketcap": 0},
        {"stock": "WMT", "marketcap": 0},
        {"stock": "LLY", "marketcap": 0},
        {"stock": "JPM", "marketcap": 0},

    ]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    for stock in stocks:
        stock['marketcap'] = 0 + yf.Ticker(stock['stock']).info['marketCap']
    stocks.sort(key=lambda x: x['marketcap'], reverse=True)
    return templates.TemplateResponse(
	  request=request, name="index.html", context={"stocks":stocks}
	)


#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=5025)
