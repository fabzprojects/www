from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api=Api(app)

@app.route('/',methods=['GET', 'POST'])
def index():
    return 'Web App with Python Flask!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)