  
from flask import Flask 
from flask import render_template
from flask import redirect
from flask import request
from flask_pymongo import PyMongo
import scrape_mars
import pymongo
from pymongo import MongoClient


# Create an instance of Flask
app = Flask(__name__, template_folder = "template")

# Use pymongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_facts"
mongo = PyMongo(app)



# Route to render index.html template using data from Mongo

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"
 


if __name__ == "__main__":
    app.run(debug=False)