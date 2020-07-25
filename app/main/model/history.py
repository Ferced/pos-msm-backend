from .. import db

class History(db.Model):
    """ history model for storing all usage of the aplication """
    __tablename__ = "history"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    document= db.Column(db.String(50))
    health_care_name = db.Column(db.String(255))
    patient_name = db.Column(db.String(150))
    service_name = db.Column(db.String(150))
    info= db.Column(db.Boolean)
    registered_on = db.Column(db.DateTime, nullable=False)