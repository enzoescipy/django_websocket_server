from websocket import WebSocketApp
from threading import Thread
import json
import time


def on_message(ws, msg):
    print(msg)
    # msg = json.loads(msg.decode('utf-8'))
def on_error(ws, msg):
    print(msg)
def on_close(ws, e0, e1):
    print("close")
def on_open(ws):
    def run(*args):
        request = '{"message": "hello, world!"}'
        for i in range(10):
            ws.send(request)
            time.sleep(1)
    th = Thread(target=run, daemon=True)
    th.start()

if __name__ == "__main__":
    ws = WebSocketApp("ws://127.0.0.1:8000/ws/chat/",
                      on_message=on_message,
                      on_error=on_error,
                      on_close=on_close,
                      on_open=on_open)
    ws.run_forever()

