import requests
import re
from app.main import db
from app.main.model.history import History
from app.main.config import puco_config
from ..service.history_service import HistoryService

class PucoService():
    def get_puco(document):
        data = []
        counter = 0
        s = requests.Session()
        payload = {'documento':document}
        url = puco_config["url"]
        request = s.post(url,data=payload)
        response_data = request.json()
        if response_data:
            for element in response_data:
                data.append({"document":document,"patient_name":response_data[counter]["NombreYApellido"],"health_care_name":response_data[counter]["NombreObraSocial"], "info":True})
                counter +=1
        else:
            data = [{"document":document,"patient_name":"","health_care_name":"", "info":False}]
        for element in data:
            HistoryService.save_new(element,"Padron Unico Consolidado (PUCO)")

        return data