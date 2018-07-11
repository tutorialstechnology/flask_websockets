from app import socketio
from flask_socketio import send, emit


@socketio.on('client_connected')
def handle_client_connect_event(json):
    print('received json: {0}'.format(str(json)))


@socketio.on('message')
def handle_json_button(json):
    # it will forward the json to all clients.
    send(json, json=True)


@socketio.on('alert_button')
def handle_alert_event(json):
    # it will forward the json to all clients.
    print('Message from client was {0}'.format(json))
    emit('alert', 'Message from backend')
