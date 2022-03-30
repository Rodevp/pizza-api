from flask import Flask
from routes.orders import orders

app = Flask(__name__)
app.register_blueprint(orders, url_prefix='/api')

@app.route('/', methods=['GET'])
def index() :
    return "OK"


PORT = 3001

if __name__ == '__main__' :
    app.run(debug=True, port=PORT)