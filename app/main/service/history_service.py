import uuid
from flask import jsonify
from app.main import db
from app.main.model.history import History
import datetime

class HistoryService():

    def get_all_searchs():
        return History.query.all()

    def get_searchs_by_info(info):
        searchs_by_info= History.query.filter_by(info=info).all()
        return searchs_by_info
    def save_new(data,service_name):
        new_search = History(
            document=data['document'],
            patient_name=data['patient_name'],
            health_care_name=data['health_care_name'],
            service_name = service_name,
            info=data['info'],
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(new_search)
        db.session.commit()