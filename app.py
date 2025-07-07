from flask import Flask

app = Flask(__name__)


@app.route("/info")
def lwinfo():
	return  "i m lw"

def lwphone():
	return"1376557627"

app.run(host="0.0.0.0")
