from flask import Flask
#pip3 install flask

app = Flask(__name__)

@app.route("/")
def elice():
    return "hellow elice"

if __name__ == "__main__":
    app.run()