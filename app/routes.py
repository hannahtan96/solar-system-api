from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, distance_from_sun):
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_sun = distance_from_sun

planets = [
    Planet(1, "Mercury", "The first planet from the sun", 35),
    Planet(2, "Venus", "The second planet from the sun", 67),
    Planet(3, "Earth", "The best planet", 93),
    Planet(4, "Mars", "The red planet", 142),
    Planet(5, "Jupiter", "The biggest one", 484)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_list_of_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance from sun (in millions of mi)": planet.distance_from_sun
            }
        )
    
    return jsonify(planets_response)


