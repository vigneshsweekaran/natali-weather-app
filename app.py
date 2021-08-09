import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

color = "#16a085"

@app.route("/")
def hello():

    url = "https://weatherapi-com.p.rapidapi.com/timezone.json"
    querystring = {"q":"<REQUIRED>"}
    headers = {
        'x-rapidapi-key': "{x-rapidapi-key}",
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    return render_template('index.html', contents=response.text, color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
