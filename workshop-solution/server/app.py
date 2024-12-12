import pickle
import logging
import warnings
import pandas as pd
from typing import Tuple
from flask import Flask, jsonify, request, Response

warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load model from pickle file
model = pickle.load(open('model.pkl', 'rb'))

# Load airports data
airports_df = pd.read_csv('origin_airport.csv')

@app.route('/')
def home():
    return "Let's build an api!"

@app.route('/airports', methods=['GET'])
def get_airports() -> Response:
    """Get list of all airports and their IDs.
    
    Returns:
        JSON response with array of airport objects
    """
    try:
        airports = airports_df.to_dict('records')
        return jsonify(airports), 200
    except Exception as e:
        logging.error(f'Error fetching airports: {str(e)}')
        return jsonify({
            'error': 'Internal server error'
        }), 500

@app.route('/predict', methods=['GET'])
def predict() -> Response:
    """Predict flight delay probability based on day and airport.
    
    Returns:
        JSON response with prediction certainty and delay percentage
    """
    try:
        # Validate input parameters
        day = request.args.get('day', type=int)
        airport = request.args.get('airport', type=int)
        
        if not day or not airport:
            return jsonify({
                'error': 'Missing required parameters: day and airport'
            }), 400
            
        if not 1 <= day <= 7:
            return jsonify({
                'error': 'Day must be between 1 and 7'
            }), 400
        
        # Make prediction
        prediction = model.predict_proba([[day, airport]])[0]
        
        # Process prediction values
        pred_parts = str(prediction).split(' ')
        certainty = round(float(pred_parts[0][1:]), 3)  # 3 decimal places
        delayed = round(float(pred_parts[1][:-1]), 3)
        
        logging.info(f'Prediction made for day:{day} airport:{airport}')
        
        return jsonify({
            'prediction_certainty': certainty,
            'delayed_percentage': delayed,
            'input': {
                'day': day,
                'airport': airport
            }
        }), 200
        
    except Exception as e:
        logging.error(f'Prediction error: {str(e)}')
        return jsonify({
            'error': 'Internal server error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)