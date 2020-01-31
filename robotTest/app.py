
from socketIO_client import SocketIO

sio=SocketIO('localhost',8000)

username = "victor"

sio.emit("auth",username)

@sio.on_connect()
def on_connect():
	breakpoint()
	print("HI")
	sio.emit("auth",username)

@sio.on('message')
def on_message(msg):
    print(msg)




