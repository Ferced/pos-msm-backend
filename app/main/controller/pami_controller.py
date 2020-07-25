from flask import request
from flask_restplus import Resource
from ..util.dto import PamiDto
from ..service.pami_service import PamiService

api = PamiDto.api
pami = PamiDto.pami

@api.route('/<documento>')
@api.param('documento', 'document to find')
class Puco(Resource):
    @api.doc('get info from pami with a document number')
    @api.marshal_with(pami)
    def get(self,documento):
        """Gets puco health care"""
        return PamiService.get_pami(documento)