from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Flask
from flask_cors import CORS, cross_origin
import flask
import sys
from MH_OPTIMIZER.coordinator import main
app = Flask(__name__)
cors = CORS(app)

@app.route('/send_data', methods=['POST'])
def send_data():

    data = request.get_json()#list of dicts
    print(data,file=sys.stderr)
    x=[]
    for d in data:
        for k,v in d.items():
            x.append((k,v))
#[{'WeaknessExploit': 3}, {'Agitator': 3}]

    results = main(x)

    return results
    # Process the data if necessary
    # ...
    


@app.route("/")
def helloWorld():
    response = flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # Process the data if necessary
    # ...
if __name__ == "__main__":
    app.run(debug=True)
