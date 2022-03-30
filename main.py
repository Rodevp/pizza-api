from flask import Flask
from db import init_db
from routes.orders import orders

app = Flask(__name__)

#db
c = init_db()

#routes
app.register_blueprint(orders, url_prefix='/api')

@app.route('/', methods=['GET'])
def index() :
    return "OK"


PORT = 3001

if __name__ == '__main__' :
    app.run(debug=True, port=PORT)