import requests
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

color = "#16a085"

@app.route("/")
def hello():

    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    querystring = {"lon":"38.5","lat":"-78.5"}
    headers = {
        'x-rapidapi-key': "cd1c88eda0msh32b10551c600641p14a147jsnc57be3d23020",
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

    obj = json.loads(response.text)
    json_formatted_str = json.dumps(obj, indent=4)
    print(json_formatted_str)

    return render_template('index.html', contents=json_formatted_str, color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
