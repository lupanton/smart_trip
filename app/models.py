from app import db

class Trip(db.Model):
    __tablename__ = 'trips'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(5000))
    date_begin = db.Column(db.Date(), nullable=False)
    date_end = db.Column(db.Date())
    is_all_inc = db.Column(db.Boolean(), default=True)

    def __init__(self, name, description, date_begin, date_end, is_all_inc):
        self.name = name
        self.description = description
        self.date_begin = date_begin
        self.date_end = date_end
        self.is_all_inc = is_all_inc