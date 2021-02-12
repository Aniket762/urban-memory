from sys import stderr
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def route():
    if request.method == "POST":
        area = int(request.form['area'])
        age = int(request.form['age'])
        bedrooms = int(request.form['bedrooms'])
        output = model.predict([[area, bedrooms, age]])
    # output2 = model.predict([[2000, 3, 4]])
    else:
        output = 0
    return render_template('index.html', pred="The price of the house is {}".format(output))


if __name__ == '__main__':
    app.run(debug='True')
