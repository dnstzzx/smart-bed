from flask import Flask, request
import json

from state import state
import msg
import cap
import cv2

app = Flask(__name__)
def run():
    app.run('0.0.0.0')

@app.route('/hello')
def hello():
    return 'hello'

@app.route('/state')
def total_state():
    return state.state_out()

@app.route('/sensor_state', methods=['GET', 'POST'])
def sensor_state():
    if request.method == 'POST':
        text = request.get_data().decode()
        state.sensor_in(text)
        return ''

@app.route('/msg_count/<role>')
def msg_count(role):
    return str(msg.msg_count(role))

@app.route('/pop_msg/<role>')
def pop_msg(role):
    return msg.pop_msg(role)

@app.route('/pop_msgs/<role>')
def pop_msgs(role):
    return json.dumps(msg.pop_msgs(role))

@app.route('/send_msg/<role>', methods=['POST'])
def send_msg(role):
    text = request.get_data().decode()
    msg.add_msg(role, text)
    return None
    
@app.route('/video')
def video():
    frame = cap.caps['cap']
    ret, frame = cv2.imencode('.jpg', frame)
    return frame.tobytes()