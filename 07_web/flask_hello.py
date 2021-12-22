from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("first_and_second.html")

@app.route("/<num>")
def first(num: str):
    return render_template("num.html", num=num.upper())


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