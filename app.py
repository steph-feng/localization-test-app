from flask import Flask
from i18nilize import Localize

app = Flask(__name__)


@app.route('/')
def hello_world():
    return Localize.translate('Hello', 'french')

if __name__ == '__main__':
    app.run()
