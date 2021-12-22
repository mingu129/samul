from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 17
LED_PIN2 = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.setup(LED_PIN2, GPIO.OUT) 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/led/red/<led>")
def redled(led : str):
    if(led == "on"):
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
    return render_template("led.html", color="RED",led=led.upper())

@app.route("/led/blue/<led2>")
def blueled(led2 : str):
    if(led2 == "on"):
        GPIO.output(LED_PIN2, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN2, GPIO.LOW)
    return render_template("led.html", color="BLUE", led=led2.upper())

if __name__ == "__main__":
    app.run(host="0.0.0.0")



