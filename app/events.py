from app import sio
from app.models import User
import pdb
from flask_socketio import join_room, rooms
lookup_room = dict()

""" When a client connects it sends back a message to join the room """
@sio.on("connect")
def connect():
    sio.emit("join room")

""" Robot triggers this to send a message to the room """
@sio.on("robot message")
def robot_message(msg):
    user = User.query.filter_by(username=msg['username']).first()
    if user != None:
        sio.emit('message',msg['message'],room=lookup_room[user.username+user.password_hash])


""" client triggers this to send a message to the room """
@sio.on("client message")
def client_message(msg):
    user = User.query.filter_by(username=msg['username'], password_hash=msg['password_hash']).first()
    if user != None:
        sio.emit('message',msg['message'],room=lookup_room[user.username+user.password_hash])





# Called to establish/connects the client in a room
# parm - cred['username'] and cred['password_hash']

@sio.on("connect client")
def connect_bot(creds):
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
        lookup_room[user.username+user.password_hash] = room
        join_room(room)
        sio.emit("message","room " + room + " configured",room=room)






# Called to bot establish/connects the bot in a room
# parm - cred['username'] and cred['password'] 

@sio.on("connect bot")
def connect_bot(creds):
    username=creds['username']
    password=creds['password']
    user = User.query.filter_by(username=username).first()
    # case 1 - check to see if a user exists
    if user is None:
        sio.emit("message","No valid username found")
    # case 2 - check to see if the password is valid
    elif user.check_password(password) is False:
        sio.emit("message","password not valid")
    else:
        room = user.username
        lookup_room[user.username+user.password_hash] = room
        join_room(room)
        sio.emit("message","room " + room + " configured",room=room)



    