from app.models.planet import Planet
import pytest
from werkzeug.exceptions import HTTPException
from app.routes import validate_planet

def test_get_all_planets_with_no_record(client):
    response = client.get("/planets")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_from_three_saved_planets(client, three_saved_planets):
    #ACT
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Asset
    assert response.status_code == 200
    assert response_body == {"id": 1, "name": "Mercury", "description": "First planet from the sun", "distance_from_sun": 35}

def test_get_one_planet_with_empty_db(client):
    #ACT
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"msg": f"Planet 1 not found"}

def test_get_all_planets_with_three_saved_planets(client, three_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body[0] == {"id": 1, "name": "Mercury", "description": "First planet from the sun", "distance_from_sun": 35}
    assert response_body[1] == {"id": 2, "name": "Venus", "description": "Second planet from the sun", "distance_from_sun": 67}
    assert response_body[2] == {"id": 3, "name": "Earth", "description": "Third planet from the sun", "distance_from_sun": 93}

def test_create_one_planet(client):
    response = client.post("/planets", json={"name": "Mercury", "description": "First planet from the sun", "distance_from_sun": 35})
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {'msg': f'Planet Mercury was successfully created.'}