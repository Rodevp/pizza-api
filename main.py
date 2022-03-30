from crypt import methods
import flask


from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index() :
    return "OK"


PORT = 3001

if __name__ == '__main__' :
    app.run(debug=True, port=PORT)