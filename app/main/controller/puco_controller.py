from flask import request
from flask_restplus import Resource
from ..util.dto import PucoDto
from ..service.puco_service import PucoService

api = PucoDto.api
puco = PucoDto.puco

@api.route('/<documento>')
@api.param('documento', 'document to find')
class Puco(Resource):
    @api.doc('get info from puco with a document number')
    @api.marshal_with(puco)
    def get(self,documento):
        """Gets puco health care"""
        return PucoService.get_puco(documento)