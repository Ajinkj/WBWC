from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forward')
def forward():
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.HIGH)
    return 'Moving forward'

@app.route('/backward')
def backward():
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(4, GPIO.HIGH)
    return 'Moving backward'

@app.route('/left')
def left():
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    return 'Moving left'

@app.route('/right')
def right():
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(4, GPIO.LOW)
    return 'Moving right'

@app.route('/stop')
def stop():
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    return 'Stopped'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
