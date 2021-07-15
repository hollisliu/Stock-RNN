import websocket
import json

def on_message(ws, message):
    try:
        data = json.loads(message)['data']
        for d in data:
            print(d['s'], d['p'], d['v'])
    except:
        print('receive error')

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:DOGEUSDT"}')
    # ws.send('{"type":"subscribe","symbol":"AAPL"}')
    # ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    # ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c0b508n48v6sc0gs4vhg",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()