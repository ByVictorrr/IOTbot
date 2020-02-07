from app import sio
from app.models import User
import pdb
from flask_socketio import join_room, rooms
# [password] - > sid_bot 
lookup_room = dict()


@sio.on("message")
def handle_message(msg):
    #msg[0] = actual message
    #msg[1] = password
    breakpoint()
    sio.emit('message',msg[0],room=lookup_room[msg[1]])

# this get the sid sent back to client
@sio.on("join")
def connect_bot(index):
    if index in lookup_room:
        room=lookup_room[index]
        join_room(room)
        sio.emit("message","bot connected", room=lookup_room[index])
    else:
        sio.emit("message", "bot couldn't connect")




#For robot interaction
@sio.on("setup room")
def set_up_bot(data):
    breakpoint()
    add_to_lookup_room(data['username'], data['password'])
    

"""
Description: a way for the arduino to give acess to user to it using sid
"""
def add_to_lookup_room(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user is None:
        sio.emit("message","No valid username found")
    else:
        room = username
        lookup_room[user.password] = room
        join_room(room)
        sio.emit("message","room " + room + " configured",room=room, namespace='/')

