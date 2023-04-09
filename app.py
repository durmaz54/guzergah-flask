from flask import Flask, render_template, url_for, send_file, request, jsonify, make_response
from agv import AGV2FLUTTER
import time
import threading
import base64
SLEEP_TIME = 1

app = Flask(__name__)

agv1 = AGV2FLUTTER()
img = "static/test1.jpg"


@app.route('/map', methods=['GET', 'POST'])
def lionel():
    print(agv1.image)
    return send_file(agv1.image)


@app.route('/agv', methods=["GET", "POST"])
def agv():

    data = agv1.readJson()
    return jsonify(data)

@app.route('/flutter', methods=["GET", "POST"])
def flutter():
    return "selam"

def startServer():
    app.run(use_reloader = False,threaded = True, host="0.0.0.0")

def loop():
    i = 1
    while True:
        time.sleep(SLEEP_TIME)
        agv1.startTimeSecond += 3
        if(agv1.startTimeSecond > 10000):
            agv1.startTimeSecond = 0
        i+=1
        if(i > 3):
            i=1
        with open("static/test{i}.jpg".format(i=i), "rb") as img_file:
            my_string = base64.encodebytes(img_file.read()).decode('utf-8')
        agv1.image = my_string
        



t1 = threading.Thread(target=loop)
t2 = threading.Thread(target=startServer)
t1.start()
t2.start()
