from flask import request
from flask_restplus import Resource
from ..util.dto import SpinDto
from ..service.spin_service import SpinService

api = SpinDto.api
spin = SpinDto.spin

@api.route('/<documento>')
@api.param('documento', 'document to find')
class Spin(Resource):
    @api.doc('get info from spin with a document number')
    @api.marshal_with(spin)
    def get(self,documento):
        """Gets spin health care"""
        return SpinService.get_spin(documento)


