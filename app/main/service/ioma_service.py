
import requests
import re
from app.main import db
from app.main.model.history import History
from app.main.config import ioma_config
from ..service.history_service import HistoryService

class IomaService():
    # TODO: QUE AGARRE LA URL DE UN CONFIG
    def get_ioma(document):
        data_found = False
        data = []
        sexo = 1
        while sexo < 3 and data_found == False:
            data = {' T3':document,'sexo':str(sexo),'B13':'Buscar'}
            url=ioma_config["url"]
            s = requests.Session()
            request = s.post(url,data=data)
            response_data = request.text
            list_data = re.findall(r'<span class="texto-azul">(.*?)</span>', response_data)
            if list_data:
                data_found=True
                data = [{"document":document,"patient_name":list_data[0].strip(),"health_care_name":"IOMA", "info":True}]
            else:
                data = [{"document":document,"patient_name":"","health_care_name":"", "info":False}]
            sexo += 1
        HistoryService.save_new(data[0],"Instituto de Obra Medico Asistencial (IOMA)")
        return data