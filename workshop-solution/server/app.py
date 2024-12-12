import pickle
import warnings
from flask import Flask

warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load model from pickle file
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Let's build an api!"


if __name__ == '__main__':
    app.run(debug=True)