from flask import Flask, request
from web import utils

app = Flask(__name__)


@app.route('/jarvis', methods=['POST'])
def jarvisinput():
    cmd = request.args.get('cmd')
    return utils.process_input(cmd)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5000)
