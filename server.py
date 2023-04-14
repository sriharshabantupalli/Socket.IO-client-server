import eventlet
import random
import socketio
# We should install packages:
# pip install eventlet
# pip install python-socketio


sio = socketio.Server()
# It creates a new 'socketio.server' object named 'sio',will handle incoming Socket.IO connections
app = socketio.WSGIApp(sio)
# This creates a object named app,used to wrap the object and enable it to used with WSGI server



# When client connects to server,it takes argument which is session ID of the connecting client
# It then emits a Random value event to the client which is a single key-value pair
@sio.on('connect')
def on_connect(sid):
    print('Client connected:', sid)

# Emit a random value to the client when it connects
    sio.emit('random_value', {'value': random.randint(1, 100)}, room=sid)



# It is called whenever a client disconnects from the Socket.IO server
@sio.on('disconnect')
def on_disconnect(sid):
    print('Client disconnected:', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)