import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

color = "#16a085"

@app.route("/")
def hello():

    url = "https://weatherapi-com.p.rapidapi.com/search.json"
    querystring = {"q":"Paris"}
    headers = {
        'x-rapidapi-key': "cd1c88eda0msh32b10551c600641p14a147jsnc57be3d23020",
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    return render_template('index.html', contents=response, color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
