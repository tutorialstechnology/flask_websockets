# -*- coding: utf-8 -*-
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

from views import index
from websockets import (
    handle_client_connect_event,
    handle_json_button,
    handle_alert_event
)
