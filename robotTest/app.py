from socketio import Client

sio=Client()
sio.connect('http://localhost:5000')

username = "victor"

@sio.event
def connect():
	breakpoint()
	sio.emit("auth", data={'username': username, 'sid': sio.sid})

@sio.on('message')
def on_message(msg):
	breakpoint()
	print(msg)




