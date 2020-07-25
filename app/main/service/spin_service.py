import requests
import re
from app.main import db
from app.main.model.history import History
from app.main.config import spin_config
from ..service.history_service import HistoryService

class SpinService():
    def get_spin(document):
        user_spin =  spin_config["user_spin"]
        password_spin = spin_config["password_spin"]
        url = spin_config["url"]
        s = requests.Session()
        #me logeo a la pagina de superintendencia
        payload = {'_user_name_':user_spin, '_pass_word_': password_spin}
        r = s.post(url, data=payload, verify=False)
        #ya logeado le mando el form data directamente con los datos que quiero buscar
        payload = {'nro_doc': document, 'B1': 'Consultar','cuil_b':'','pagina_consulta':''}
        r = s.post(url, data=payload, verify=False)
        content_text = r.text
        #filtro el HTML completo que me devuelve en busca de los tag que contienen informacion
        list_data = re.findall(r'<td>(.*?)</td>', content_text)
        #chequeo que el list_data tenga informacion
        if "No se reportan datos para el NUMERO DE DOCUMENTO" in content_text:
            data = [{"document":document,"patient_name":"NULL","health_care_name":"NULL", "info":False}]
        else:
            nombre= list_data[5].strip()
            #filtro de vuelta para buscar el resto de la informacion
            list_data = re.findall(r'<td><b>(.*?)</b></td>', content_text)
            obra_social = list_data[2].strip()
            data =  [{"document":document,"patient_name":nombre,"health_care_name":obra_social, "info":True}]
        HistoryService.save_new(data[0],"Superintendencia de la salud (SPIN)")
        return data

