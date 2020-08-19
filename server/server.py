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


if __name__ == "__main__":
	print("Starting Python Flask Server for Home Price Prediction")
	app.run()