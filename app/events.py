from app import sio
from app.models import User
import pdb
from flask_socketio import join_room, rooms, leave_room
from flask import request

# multiple sid may point to the same room name 
lookup_room = dict()
# used to determine if the client has connected
rooms = set()

""" When a client connects it sends back a message to join the room """
@sio.on("connect")
def connect():
    sio.emit("join room")

@sio.on("disconnect")
def disconenct():
    breakpoint()
    if request.sid in lookup_room:
        leave_room(lookup_room[request.sid])
        del lookup_room[request.sid]

""" triggers this to send a message to the room """
@sio.on("message")
def message(msg):
    if request.sid in lookup_room:
        sio.emit('message', msg,room=lookup_room[request.sid])
    else:
        sio.emit("join room")


# gets triggered when the client disconnects
@sio.on("remove room")
def remove_room():
    breakpoint()
    # step 1 - remove creds to that rooms
    room = lookup_room[request.sid]
    if room is not None and room in rooms:
        rooms.remove(room)
        leave_room(room)
        del lookup_room[request.sid]
        sio.emit('disconnect', room=room)


# Called to establish/connects the client in a room
@sio.on("connect client")
def connect_client(creds):
    sid = request.sid
    username=creds['username']
    password_hash=creds['password_hash']
    user = User.query.filter_by(username=username).first()
    # case 1 - check to see if a user exists
    if user is None:
        sio.emit("message","No valid username found")
    # case 2 - make sure the password is valid
    elif user.password_hash != password_hash:
        sio.emit("message","password not valid")
    else:
        room = user.username
        lookup_room[sid] = room
        join_room(room)
        rooms.add(room)
        sio.emit("message","room " + room + " configured",room=room)
    


# Called to bot establish/connects the bot in a room
# parm - cred['username'] and cred['password'] 
@sio.on("connect bot")
def connect_bot(creds):
    # step 1 - get the sid of the client 
    sid = request.sid
    username=creds['username']
    password=creds['password']
    user = User.query.filter_by(username=username).first()
    # case 1 - check to see if a user exists
    if user is None:
        sio.emit("message","No valid username found")
    # case 2 - check to see if the password is valid
    elif user.check_password(password) is False:
        sio.emit("message","password not valid")
    # case 3 - check to see if the room is setup by the client
    elif username not in rooms:
        sio.emit("message", "have client setup the room first")
        sio.emit("join room")
    else:
        # get sid from client
        room = user.username
        lookup_room[sid] = room
        join_room(room)
        sio.emit("message","bot connected to " + room ,room=room)



    