import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING":True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

        with app.app_context():
            db.create_all()
            yield app

        with app.app_context():
            db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def three_saved_planets(app):
    mercury = Planet(name="Mercury", description="First planet from the sun", distance=35)
    venus = Planet(name="Venue", description="Second planet from the sun", distance=67)
    earth = Planet(name="Earth", description="Third planet from the sun", distance=93)

    db.session.add_all([mercury, venus, earth])
    db.session.commit()






