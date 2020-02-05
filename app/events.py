from app import sio
from app.models import User
import pdb

lookup_bot = dict()

"""
@sio.on('connect')
def connect():
    print("connecting!")
    sio.emit('connect','authorized complete')
    """


@sio.on("message")
def handle_message(msg):
    pass
    #breakpoint()


#For robot interaction
# data = "{username, sid}"
@sio.on("auth")
def set_up_bot(data):
    #breakpoint()
    add_to_lookup_bot(data['sid'],data['username'])

# this get the sid sent back to client
@sio.on("connect bot")
def connect_bot(user):
    #breakpoint()
    sio.emit("connect bot", lookup_bot[user])




"""
Description: a way for the arduino to give acess to user to it using sid

    Given Cred(username, pasword) and sid(of the bot),
        add to the dictionary st: lookup_bot[user] = sid of bot
"""
def add_to_lookup_bot(sid, username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        emit("message","No valid username found" ,room=sid)
    else:
        # add to the dictonary(object = User: "sid")
        lookup_bot[user.username] = sid

