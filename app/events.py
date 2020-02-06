from app import sio
from app.models import User
import pdb
from flask_socketio import join_room
# [key is username] - > value: room name
lookup_room = dict()


@sio.on("message")
def handle_message(msg):
    breakpoint()
    sio.emit('message',msg[0],room=lookup_room[(msg[1], msg[2])])

# this get the sid sent back to client
@sio.on("connect bot")
def connect_bot(user):
    sio.emit("connect bot", lookup_bot[user])


#For robot interaction
@sio.on("setup room")
def set_up_bot(data):
    add_to_lookup_room(data['sid'],data['username'])
    

"""
Description: a way for the arduino to give acess to user to it using sid

    Given Cred(username, pasword) and sid(of the bot),
        add to the dictionary st: lookup_bot[user] = sid of bot
"""
def add_to_lookup_room(sid, username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        emit("message","No valid username found" ,room=sid)
    else:
        lookup_room[(user.username,user.password)] = sid 
        join_room(sid)

