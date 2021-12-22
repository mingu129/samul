from flask import Flask, render_template, request
import RPi.GPIO as GPIO

LED_PIN = 17
LED_PIN2 = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.setup(LED_PIN2, GPIO.OUT) 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("button.html")

@app.route("/led/<color>/<led>")
def first(color, led):
    if color == "red":
        led1 = LED_PIN2
    elif color == "blue":
        led1 = LED_PIN
    
    if led == "on":
        # print("on")
        GPIO.output(led1, GPIO.HIGH)
        return "LED ON"
    elif led == "off":
        GPIO.output(led1, GPIO.LOW)
        return "LED OFF"


if __name__ == "__main__":
    app.run(host="0.0.0.0")



# function register(){
# 	var menu = document.getElementById("menu").value;
# 	var price = document.getElementById("price").value;
# 	var pay = document.getElementById("pay").value;
	
#     var obj={"menu":menu,"price":price,"pay":pay};
    
#     //POST 데이터를 보낼 url - ex) localhost/register
# 	fetch('/register', {
# 		method: 'POST',
# 		headers: {
# 			'Content-Type': 'application/json'
# 		},
# 		body: JSON.stringify({
# 			data:obj			
# 		})
# 	});
# }