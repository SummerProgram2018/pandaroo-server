from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from config import get_configuration
from rest_server import REST_blueprint
import sys 


def route_socketio(socketio): 
    @socketio.on('my event', namespace='/test')
    def test_message(message):
        emit('my response', {'data': message['data']})
    
    @socketio.on('my broadcast event', namespace='/test')
    def test_message(message):
        emit('my response', {'data': message['data']}, broadcast=True)
    
    @socketio.on('connect', namespace='/test')
    def test_connect():
        emit('my response', {'data': 'Connected'})
    
    @socketio.on('disconnect', namespace='/test')
    def test_disconnect():
        print('Client disconnected')
    
def main(arg):
    app = Flask(__name__)
    app.register_blueprint(REST_blueprint())
    app.config.update(get_configuration("config.json", "DEFAULT"))
    socketio = SocketIO(app)
    route_socketio(socketio)
    socketio.run(app, host=app.config["HOST"], port=app.config["PORT"])

if __name__ == '__main__':
    main(sys.argv)


