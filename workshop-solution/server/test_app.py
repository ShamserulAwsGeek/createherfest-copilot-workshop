import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route returns correct message"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Let's build an api!"

def test_airports_route(client):
    """Test the airports route returns paginated airport data"""
    response = client.get('/airports')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert 'airports' in data
    assert 'page' in data
    assert 'per_page' in data
    assert 'total' in data
    assert len(data['airports']) <= data['per_page']

def test_airports_pagination(client):
    """Test airports pagination works correctly"""
    response = client.get('/airports?page=2&per_page=5')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['page'] == 2
    assert data['per_page'] == 5
    assert len(data['airports']) <= 5

def test_predict_route_success(client):
    """Test successful prediction"""
    response = client.get('/predict?day=1&airport=14771')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert 'prediction_certainty' in data
    assert 'delayed_percentage' in data
    assert 'input' in data
    assert data['input']['day'] == 1
    assert data['input']['airport'] == 14771

def test_predict_missing_params(client):
    """Test prediction with missing parameters"""
    response = client.get('/predict')
    data = json.loads(response.data)
    
    assert response.status_code == 400
    assert 'error' in data
    assert data['error'] == 'Missing required parameters: day and airport'

def test_predict_invalid_day(client):
    """Test prediction with invalid day"""
    response = client.get('/predict?day=8&airport=14771')
    data = json.loads(response.data)
    
    assert response.status_code == 400
    assert 'error' in data
    assert data['error'] == 'Day must be between 1 and 7'
