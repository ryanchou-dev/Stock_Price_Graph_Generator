
import plotly.graph_objs as go

#Data Source
import yfinance as yf
import PySimpleGUI as sg
error_message = ""
sg.change_look_and_feel('DarkBlue2')
layout=[
    [sg.Text("Write a stock symbol: ")],
    [sg.InputText(key='symbol')],
    [sg.Text(error_message)],
    [sg.Button('Submit'), sg.Button('Cancel')]
]

window = sg.Window("Stock Price Tracker", layout, resizable=True, element_justification="c").Finalize()
window.Maximize()

while True:
    event, value = window.Read()
    if event in (None, 'Cancel'):
        break
    if event == 'Submit':
    
        choice = value['symbol']
        choice = choice.upper()
        data = yf.download(tickers=choice, period = '5d', interval = '15m', rounding= True)
        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=data.index,open = data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name = 'market data'))
        fig.update_layout(title = choice + ' share price', yaxis_title = 'Stock Price (USD)')
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label='15m', step="minute", stepmode="backward"),
                    dict(count=45, label='45m', step="minute", stepmode="backward"),
                    dict(count=1, label='1h', step="hour", stepmode="backward"),
                    dict(count=6, label='6h', step="hour", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        fig.show()
