from app import socketio
from flask_socketio import send, emit


@socketio.on('client_connected')
def handle_client_connect_event(json):
    print('received json: {0}'.format(str(json)))


@socketio.on('json_button')
def handle_json_button(json):
    send(json, json=True)


@socketio.on('alert_button')
def handle_alert_event(json):
    emit('alert', json)
