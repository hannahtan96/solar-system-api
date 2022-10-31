from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet
# comment
# class Planet:
#     def __init__(self, id, name, description, distance_from_sun):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance_from_sun = distance_from_sun

# planets = [
#     Planet(1, "Mercury", "The first planet from the sun", 35),
#     Planet(2, "Venus", "The second planet from the sun", 67),
#     Planet(3, "Earth", "The best planet", 93),
#     Planet(4, "Mars", "The red planet", 142),
#     Planet(5, "Jupiter", "The biggest one", 484)
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])
# def get_list_of_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(
#             {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "distance from sun (in millions of mi)": planet.distance_from_sun
#             }
#         )
    
#     return jsonify(planets_response)

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"msg": f"Planet {planet_id} is not valid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     abort(make_response({"msg": f"Planet {planet_id} not found"}, 404))


# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "distance from sun (in millions of mi)": planet.distance_from_sun
#         }, 200


@planets_bp.route("", methods=["POST"])
def create_one_planet():
    request_body = request.get_json()

    new_planet = Planet(
        name=request_body['name'],
        description=request_body['description'],
        distance_from_sun=request_body['distance_from_sun']
    )

    db.session.add(new_planet)
    db.session.commit()

    return jsonify({'msg': f'Planet {new_planet.name} was successfully created.'}), 201

@planets_bp.route("", methods=["GET"])
def get_list_of_planets():
    planets = Planet.query.all()
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
    
    return jsonify(planets_response), 200

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)

    db.session.delete(planet)
    db.session.commit()
    
    return jsonify({'msg': f'Planet {planet.name} successfully deleted'})

    