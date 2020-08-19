from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def home():
	return "Home Price Prediction"

@app.route('/get_location_names')
def get_location_names():
	response = jsonify({
		'locations' : util.get_location_names()
		})
	response.headers.add('Access-Control-Allow-Orgin', '*')
	return response

@app.route('/predict_home_price', method = ['POST'])
def predict_home_price():
	total_sqft = float(request.form['total_sqft'])
	location = float(request.form['location'])
	bhk = float(request.form['bhk'])
	bath = float(request.form['bath'])

	response = jsonify({
		'estimated_price' : util.get_estimated_price(location, total_sqft, bhk, bath)
		})
	return response

if __name__ == "__main__":
	print("Starting Python Flask Server for Home Price Prediction")
	app.run()