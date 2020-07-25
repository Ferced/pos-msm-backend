from flask import request
from flask_restplus import Resource
from ..util.dto import PucoSumarDto
from ..service.puco_sumar_service import PucoSumarService

api = PucoSumarDto.api
puco_sumar = PucoSumarDto.puco_sumar

@api.route('/<documento>')
@api.param('documento', 'document to find')
class PucoSumar(Resource):
    @api.doc('get info from PucoSumar with a document number')
    @api.marshal_with(puco_sumar)
    def get(self,documento):
        """Gets PucoSumar health care"""
        return PucoSumarService.get_puco_sumar(documento)


