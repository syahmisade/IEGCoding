from flask import Flask # type: ignore

# http://127.0.0.1:5000 # kalau tak run server -> 404 Error (Not Found)
# flask run -h 172.16.0.101 -> sir jegan punya

# print("__main__")
app = Flask(__name__)

@app.route("/") # a decorator
def say():
    return "Hello Sahabat Organik!"