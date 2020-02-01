from socketio import Client

sio=Client()
sio.connect('http://localhost:5000')

username = "victor"

@sio.on('connect')
def connect():
	breakpoint()
	sio.emit("auth", data=username)
@sio.on('message')
def on_message(msg):
    print(msg)




