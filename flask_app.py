from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Dag Peter! Ik doe een wanhopig beroep op uw edele wijsheid als leerkracht!</p>"

if __name__ == "__main__":
    app.run(debug=True)
