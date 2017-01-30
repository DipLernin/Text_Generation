from flask import Flask
from flask import request
from flask.json import jsonify
from predictor import predict
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/models/<model_name>/")
def pred(model_name):
    try:
        warm_text = request.args.get('warm', default='roses are red')
        count_char = request.args.get('cchar', default='')
        if count_char == '\\n':
            count_char = '\n'
        number = int(request.args.get('num', default='10'))
        temperature = float(request.args.get('temp', default='0.5'))
    except ValueError:
        return jsonify({"error": "input error"})

    try:
        generated = predict(model_name, warm_text, count_char, number, temperature)
    except KeyError:
        return jsonify({"error": "model not fonud"})

    return jsonify({"result": generated})


if __name__ == "__main__":
    app.run(host=0.0.0.0,port='8889')
