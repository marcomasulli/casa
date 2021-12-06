from . import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(80), unique=True, nullable=True)
    app_icon_link = db.Column(db.String(255), unique=False, nullable=True)
    app_description = db.Column(db.String(255), unique=False, nullable=True)
    app_protocol = db.Column(db.String(120), unique=False, nullable=True)
    app_address = db.Column(db.String(120), unique=False, nullable=True)
    app_port = db.Column(db.Integer(), unique=False, nullable=True)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_name = db.Column(db.String(80), unique=True, nullable=True)
    profile_default_url = db.Column(db.String(80), unique=True, nullable=True)
    profile_background = db.Column(db.Integer(), unique=False, nullable=True)
    profile_columns = db.Column(db.Integer(), unique=False, nullable=True)
    profile_cards_per_row = db.Column(db.String(120), unique=False, nullable=True)
    profile_is_current = db.Column(db.Boolean(), unique=False, nullable=True)

class Background(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    background = db.Column(db.String(120), unique=True, nullable=True)
    background_class = db.Column(db.String(120), unique=True, nullable=True)

class RowStructure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row_class = db.Column(db.String(120), unique=True, nullable=True)
    row_cards = db.Column(db.Integer(), unique=True, nullable=True)

try:
    RowStructure.__table__.drop()
except Exception as e:
    print(e)

db.create_all()

""" Fill the tables values """

backgrounds = [
    {'background':'white', 'background_class':'white'},
    {'background':'light', 'background_class':'light'},
    {'background':'dark', 'background_class':'dark'},
    {'background':'light green', 'background_class':'primary'},
    {'background':'blue', 'background_class':'link'},
    {'background':'green', 'background_class':'success'},
    {'background':'yellow', 'background_class':'warning'},
    {'background':'red', 'background_class':'danger'},
    {'background':'custom', 'background_class':'custom'},
]

rows = [
    {'row_class':'is-full', 'row_cards': 1},
    {'row_class':'is-half', 'row_cards': 2},
    {'row_class':'is-one-third', 'row_cards': 3},
    {'row_class':'is-one-quarter', 'row_cards': 4},
    {'row_class':'is-one-fifth', 'row_cards': 5},
]

for background in backgrounds:
    try:
        new_value = Background(**background)
        db.session.add(new_value)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()

for row in rows:
    try:
        new_value = RowStructure(**row)
        db.session.add(new_value)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()