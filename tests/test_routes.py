from app.models.planet import Planet
import pytest
from werkzeug.exceptions import HTTPException
from app.routes import validate_planet

def test_get_all_planets_with_no_record(client):
    response = client.get("/planets")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == []

