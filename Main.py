from brain import srapWeb
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "sdfaf290992jf23093jfndf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clubs.db"
db = SQLAlchemy()
db.init_app(app)

class UEFA_GROUP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String, nullable=True)
    group = db.Column(db.String, nullable=False)
    firstPlace = db.Column(db.String(20), nullable=False)
    secondPlace = db.Column(db.String(20), nullable=False)
    thirdPlace = db.Column(db.String(20), nullable=False)
    fourthPlace = db.Column(db.String(20), nullable=False)

class EKSTRAKLASA_TOP5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String, nullable=True)
    firstPlace = db.Column(db.String(20), nullable=False)
    secondPlace = db.Column(db.String(20), nullable=False)
    thirdPlace = db.Column(db.String(20), nullable=False)
    fourthPlace = db.Column(db.String(20), nullable=False)
    fifthPlace = db.Column(db.String(20), nullable=False)


with app.app_context():
    db.create_all()






scrapWeb = srapWeb()
scrapWeb.input()
scrapWeb.choose_correct_link()


if scrapWeb.x == "UEFA":
    with app.app_context():
        new_record = UEFA_GROUP(
            time=datetime.now().strftime("%d/%m/%Y"),
            group=scrapWeb.y,
            firstPlace=scrapWeb.CLUBS[0],
            secondPlace=scrapWeb.CLUBS[1],
            thirdPlace=scrapWeb.CLUBS[2],
            fourthPlace=scrapWeb.CLUBS[3]
        )
        db.session.add(new_record)
        db.session.commit()
elif scrapWeb.x == "EKSTRAKLASA":
    with app.app_context():
        new_record = EKSTRAKLASA_TOP5(
            time=datetime.now().strftime("%d/%m/%Y"),
            firstPlace=scrapWeb.CLUBS[0],
            secondPlace=scrapWeb.CLUBS[1],
            thirdPlace=scrapWeb.CLUBS[2],
            fourthPlace=scrapWeb.CLUBS[3],
            fifthPlace=scrapWeb.CLUBS[4]
        )
        db.session.add(new_record)
        db.session.commit()
scrapWeb.driver.quit()
scrapWeb.printClubs()