from flask import Flask
from internationalize.localize import Localize

app = Flask(__name__)


@app.route('/')
def hello_world():
    return Localize.translate('hello', 'french')

if __name__ == '__main__':
    app.run()
