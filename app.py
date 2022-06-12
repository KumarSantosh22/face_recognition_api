import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from match import faceMatch
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# CORS(app, resources={r"/api/*/*": {"origins": ["*", "http://localhost:5500/"]}})
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

@app.route('/', methods=['GET'])
# @cross_origin(origin='*',headers=['Content-Type','Authorization'])
def home():
    return '''<h1>Face API</h1><p>This is a face web API</p>'''


@app.route('/api/v1/facematch', methods=['GET', 'POST'])
# @cross_origin(origin='*',headers=['Content-Type','Authorization'])
def face_match():
    try:
        if request.method == 'POST':
            content = request.json
            res = faceMatch(srcFile=content['fileData1'], destFile=content['fileData2'])
            return res
    except:
        return { 'error': ' Some error ocuured while processing. Try again...'}


if __name__ =='__main__':
    app.run(host='localhost', port=5000, debug=True)