from flask import request
from flask_restplus import Resource
from ..util.dto import IomaDto
from ..service.ioma_service import IomaService

api = IomaDto.api
ioma = IomaDto.ioma

@api.route('/<documento>')
@api.param('documento', 'document to find')
class Ioma(Resource):
    @api.doc('get info from Ioma with a document number')
    @api.marshal_with(ioma)
    def get(self,documento):
        """Gets Ioma health care"""
        return IomaService.get_ioma(documento)