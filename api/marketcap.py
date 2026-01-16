from flask import Flask, render_template,request
import yfinance as yf
import time
# import requests_cache
# session = requests_cache.CachedSession('yfinance.cache')
# session.headers['User-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

# yf.Ticker("AAPL").info['marketCap']

stocks = [
        {"stock": "AAPL", "marketcap": 0},
        {"stock": "MSFT", "marketcap": 0},
        {"stock": "AMZN", "marketcap": 0},
        {"stock": "GOOGL", "marketcap": 0},
        {"stock": "META", "marketcap": 0},
        {"stock": "TSLA", "marketcap": 0},
        {"stock": "TSM", "marketcap": 0},
        {"stock": "NVDA", "marketcap": 0},
        {"stock": "V", "marketcap": 0},
        {"stock": "JPM", "marketcap": 0},
        {"stock": "JNJ", "marketcap": 0},
    ]

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

    for stock in stocks:
        stock['marketcap'] = 0 + yf.Ticker(stock['stock']).info['marketCap']
        time.sleep(0.5)
    stocks.sort(key=lambda x: x['marketcap'], reverse=True)

    Html ="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1, user-scalable=no">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta http-equiv="refresh" content="600" />
        <link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/dark.min.css'>
    </head>
    <body>
        <h1>Top Market Cap Stocks:</h1>
        <ol>"""

    for stock in stocks:
        Html += "<li>"
        if "marketcap" in stock:
            if stock["marketcap"] > 1000000000000:
                Html += "<h3>"
        Html += f"{stock['stock']}: {stock['marketcap']}</h3></li>"

    Html += """
        </ol>
    <h2>See you at the next <a href="https://floridajs.com">FloridaJS</a> event!</h2>
    </body>
    </html>
    """
    return Html
    # if request.method == 'GET':
    #     return websiteReply("")
    # if request.method == 'POST':
    #     inputfields = request.form # a multidict containing POST data
    #     question = inputfields.get('question')
    #     return websiteReply(askQuestion(question))
    # else:
    #     Sreturn "<html><body>Something went wrong</body></html>"
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5025)
