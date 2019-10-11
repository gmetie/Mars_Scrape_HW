from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import requests
import scrape_mars



app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_HW"
mongo = PyMongo(app)
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)



@app.route("/scrape")
def scraper():
   mars = mongo.db.mars
   mars_HW = scrape_mars.scrape()
   mars.replace_one({}, mars_HW, upsert=True)
   return redirect("/", code=302)



if __name__ == "__main__":
   app.run(debug=True)