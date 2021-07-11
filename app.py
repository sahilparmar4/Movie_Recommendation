from flask import *
import pickle
import numpy as np
import pandas as pd
import goeduhub_assignment17

app = Flask(__name__)
model = pickle.load(open("recomm.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods = ["POST"])
def recommend():
    if request.method == "POST":
        movie_name =  request.form["movie"]
        result = goeduhub_assignment17.recommendation(movie_name)
        # output = "Recommended movies: \n" + result
        return result

if __name__ == "__main__":
    app.run(debug = True)
