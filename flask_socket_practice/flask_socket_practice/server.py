from flask import Flask, render_template
from flask_socketio import SocketIO , emit

app = Flask(__name__)
# Initialize SocketIO
socketio = SocketIO(app, async_mode='threading')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    # Send the message to all clients
    emit('response', message) 

def main():
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port, debug=True, ssl_context='adhoc')