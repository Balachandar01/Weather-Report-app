from flask import Flask,request,render_template
import requests
app = Flask(__name__)
@app.route("/")
def show_homepage():
    return render_template("index.html")
@app.route("/weatherapp",methods = ["GET","POST"])
def get_weather_data():
    url_ = "https://api.openweathermap.org/data/2.5/weather"
    para = {"q":request.form.get("city"),
            "appid":request.form.get("appid"),
            "units":request.form.get("units")
            }
    data =requests.get(url_,params = para)
    return f"Data:{data.json()}"
if __name__ =="__main__":
    app.run(host="0.0.0.0")


