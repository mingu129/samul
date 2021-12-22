from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/led/<led>")
def led(led):
    return render_template("led.html", led=led)



if __name__ == "__main__":
    app.run(host="0.0.0.0")