from . import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(80), unique=True, nullable=True)
    app_description = db.Column(db.String(255), unique=False, nullable=True)
    app_protocol = db.Column(db.String(120), unique=False, nullable=True)
    app_address = db.Column(db.String(120), unique=False, nullable=True)
    app_port = db.Column(db.Integer(), unique=False, nullable=True)

    def __repr__(self):
        return '<App Name %r>' % self.app_name

"""
class Preferences(db.Model):
    pass
"""

db.create_all()
