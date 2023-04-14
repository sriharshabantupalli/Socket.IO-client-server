import socketio

# creates a Socket.IO client instance
sio = socketio.Client()

# This  will be called when the client connects to the server
@sio.on('connect')
def on_connect():
    print('Connected to server')

# This will be called when the client disconnect to the server
@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

# This function call random value event from the server
# The data parameter contains any data that was sent with the event
@sio.on('random_value')
def on_random_value(data):
    print('Received random value:', data['value'])

# connect to the server
sio.connect('http://localhost:5000')

# wait for events
sio.wait()