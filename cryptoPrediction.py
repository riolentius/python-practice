from matplotlib.pyplot import title
import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go

today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=730)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download("BTC-USD", start=start_date, end=end_date, progress=False)

data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)


figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"],
                                        high=data["High"], low=data["Low"], close=data["Close"])])
figure.update_layout(title="Bitcoin price Analysis",
                     xaxis_rangeslider_visible=False)
figure.show()
