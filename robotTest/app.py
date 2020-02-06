from socketio import Client

sio=Client()
sio.connect('http://localhost:5000')

username = "victor"
password = "calpoly"

@sio.event
def connect():
	breakpoint()
	sio.emit("setup room", data={'username': username, 'sid': sio.sid})


@sio.on('message')
def on_message(msg):
	print(msg)




