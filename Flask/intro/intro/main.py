from flask import Flask
import requests

requests.get("https://www.google.com")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__": 
    app.run()

