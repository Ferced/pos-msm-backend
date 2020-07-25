from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.spin_controller import api as spin_ns
from .main.controller.puco_controller import api as puco_ns
from .main.controller.puco_sumar_controller import api as puco_sumar_ns
from .main.controller.ioma_controller import api as ioma_ns
from .main.controller.pami_controller import api as pami_ns
from .main.controller.history_controller import api as history_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='POS',
          version='2.0',
          description='aplication to search for health care providers by document'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(spin_ns)
api.add_namespace(puco_ns)
api.add_namespace(puco_sumar_ns)
api.add_namespace(ioma_ns)
api.add_namespace(pami_ns)
api.add_namespace(history_ns)
