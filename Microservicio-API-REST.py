from flask import *

app = Flask(__name__)

PORT = 3200

# Get Method

INFO = {
    "languages": {
        "es":"Spanish",
        "en":"English",
        "fr":"French",
    },
    "colors":{
        "r":"red",
        "g":"green",
        "b":"blue",
    },
    "clouds":{
        "IBM":"IBM CLOUD",
        "AMAZON":"AWS",
        "MICROSOFT":"AZURE",
    }
}

@app.route("/")
def home():
   return "<h1 style='color:blue'>This is home!</h1>"

@app.route('/temp')
def hello_world():
    return render_template('index.html')

@app.route('/qsrt')
def query_string():
    if request.args:
        req = request.args
        res = {}
        for key, value in req.items():
            res [key] = value
        res = make_response(jsonify(res), 200)
        return res

@app.route('/json')
def get_json():
    res  = make_response(jsonify(INFO), 200)
    return res

@app.route('/json/<collection>/<member>')
def get_data(collection, member):
    if collection in INFO:
        member = INFO[collection].get(member)
        if member:
            res = make_response(jsonify(member), 200)
            return res
        
        res = make_response(jsonify("No found"), 400)
        return res


if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host='0.0.0.0', port=PORT, debug=True)