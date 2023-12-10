from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
from app import routes, models

with app.app_context():
    db.create_all()
    if db.session.query(models.Trip).first() == None:
        trip1 = models.Trip("Путешествие на Плутон", "Отличная планета! Проведете незабываемую 1000 лет - бессмертие прилагается! И это ничего не стоит для Вас- ведь вы будете трудиться на на самой огромной каменоломне!", date(2025,12,15), date(3025,12,15), True)
        trip2 = models.Trip("Путешествие на Луну", "На нее воют волки и смотрят влюбленные. Стоимость всего $30 млн.", date(2024,12,12), date(2095,12,15), True)
        trip3 = models.Trip("Путешествие на Юритер", "900 лет немыслимого давления! Бессмертие прилагается. $500 млн. - дорого, но это того стоит", date(2026,11,11), date(2925,12,15), True)
        trip4 = models.Trip("Путешествие на Комеету Галлея", "Скорость, скорость, скорость!!! $900 млн - а что Вы хотите: ее еще догнать нужно", date(2030,12,12), date(3125,12,15), True)
        trip5 = models.Trip("Романтическое Путешествие на Венеру", "Это для двоих истинно влюбленных! Бессметрие прилагается обоим! Но придется повкалывать, а так бесплатно", date(2027,12,11), date(2725,12,15), True)
        trip6 = models.Trip("Путешествие на Нептун", "300 лет героического состязания со стихией. Бесплатно для Вас. Рабочее место и бессмертие прилагаются", date(2024,12,12), date(2325,12,15), True)
        db.session.add(trip1)
        db.session.add(trip2) 
        db.session.add(trip3)
        db.session.add(trip4)
        db.session.add(trip5)
        db.session.add(trip6)
        db.session.commit()
        db.session.close()

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)