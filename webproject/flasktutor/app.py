from flask import Flask # type: ignore

# http://127.0.0.1:5000 # 404 Error (Not Found)

# print("__main__")
app = Flask(__name__)

@app.route("/")
def say():
    return "Hello Sahabat Organik!"