#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
from app.main import db
from app.main.model.history import History
from app.main.config import pami_config
from ..service.history_service import HistoryService

class PamiService():
    def get_pami(document):
        provider_data = []
        data = {}
        counter = 0
        info_provider = False
        patient_name = ""
        s = requests.Session()
        payload = {'tipoDocumento':'DNI','nroDocumento':document}
        url_base=pami_config["url_base"]
        url = pami_config["url"]
        request = s.post(url,data=payload)
        response_data = request.text
        list_data = re.findall(r'<a href="(.*?)">', response_data)
        list_data = [element for element in list_data if 'result' in element and 'https' not in element]
        if len(list_data) > 0: 
            url = url_base + list_data[len(list_data)-1]
            request = s.get(url)
            response_data = request.text
            list_data = re.findall(r'<p>(.*?)</p>', response_data)
            patient_name = list_data[1] 
            data = {"document":document,"patient_name":patient_name,"health_care_name":"PAMI", "info":True}
            table_start_position = False
            table_counter = 0
            info_provider = True
            for element in list_data:
                if list_data[counter-1].strip() == "PRESTADOR:" and list_data[counter-2].strip() == "RED:":
                    table_start_position = True
                if table_counter % 3 == 0 and table_start_position == True and counter != len(list_data)-3:
                    provider_data.append({"D_MODULO":list_data[counter],"RED":list_data[counter+1], "PRESTADOR":list_data[counter+2]})
                counter += 1
                if table_start_position:
                    table_counter+=1
        else:
            info_provider = False
            data = {"document":document,"patient_name":"","health_care_name":"", "info":False}
        HistoryService.save_new(data,"Programa de Atención Médica Integral (PAMI)")
        return {"patient_name":patient_name,"provider_data":provider_data,"info":info_provider}