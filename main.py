import websocket
import json
import bitstamp.client

import credentials

def client():
    return bitstamp.client.Trading(credentials.USER,
                 credentials.KEY, credentials.SECRET)

def buy(amount):
    trading_client = client()
    trading_client.buy_market_order(amount)

def sell(amount):
    trading_client = client()
    trading_client.sell_market_order(amount)



def on_open(ws):
    print('### open to connection ###')

    json_subscribe = """
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}
"""
    ws.send(json_subscribe)


def on_message(ws, message):
    message = json.loads(message)
    price = message['data']['price']
    print(price)

    if price > 50000:
        sell()
    elif price < 38000:
        buy()
    else:
        print('waiting low or high')

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")




if __name__ == '__main__':
    ws = websocket.WebSocketApp('wss://ws.bitstamp.net',
                                on_open=on_open,
                                on_close=on_close,
                                on_error=on_error,
                                on_message=on_message)
    ws.run_forever()