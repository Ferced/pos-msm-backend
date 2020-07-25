from flask import request
from flask_restplus import Resource

from app.main.util.decorator import user_credentials_required
from ..util.dto import HistoryDto
from ..service.history_service import HistoryService

api = HistoryDto.api
history_details = HistoryDto.history

@api.route('/')
class History(Resource):
    #@user_credentials_required
    @api.marshal_list_with(history_details, envelope='data')
    def get(self):
        """List all searchs"""
        return HistoryService.get_all_searchs()


