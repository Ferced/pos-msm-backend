from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id':fields.Integer(required=False, description='user id'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class TestDto:
    api = Namespace('test', description='Just a test')
    test = api.model('test', {
        'test_message': fields.String(required=True, description='A message to send the test class'),
    })


class SpinDto:
    api = Namespace('spin', description='all actions releated to spin')
    spin = api.model('spin', {
        'patient_name': fields.String(required=False, description='name of the patient'),
        'health_care_name': fields.String(required=False, description='name of the health care provider'),
        'info': fields.Boolean(required=False, description='True if there was any information from this document')

    })

class PucoDto:
    api = Namespace('puco', description='all actions releated to puco')
    puco = api.model('puco', {
        'patient_name': fields.String(required=False, description='name of the patient'),
        'health_care_name': fields.String(required=False, description='name of the health care provider'),
        'info': fields.Boolean(required=False, description='True if there was any information from this document')

    })
class PucoSumarDto:
    api = Namespace('puco_sumar', description='all actions releated to puco sumar')
    puco_sumar = api.model('puco_sumar ', {
        'patient_name': fields.String(required=False, description='name of the patient'),
        'health_care_name': fields.String(required=False, description='name of the health care provider'),
        'info': fields.Boolean(required=False, description='True if there was any information from this document')

    })
class IomaDto:
    api = Namespace('ioma', description='all actions releated to ioma')
    ioma = api.model('ioma', {
        'patient_name': fields.String(required=False, description='name of the patient'),
        'health_care_name': fields.String(required=False, description='name of the health care provider'),
        'info': fields.Boolean(required=False, description='True if there was any information from this document')

    })
class PamiDto:
    api = Namespace('pami', description='all actions releated to pami')
    pami = api.model('pami', {
        'patient_name': fields.String(required=False, description='name of the patient'),
        'provider_data': fields.Nested(
        api.model(  'povider', {
        'D_MODULO' : fields.String(required=False,attribute='D_MODULO'),
        'RED' : fields.String(required=False,attribute='RED'),
        'PRESTADOR':fields.String(required=False,attribute='PRESTADOR')
        })
        
        ),
        'info': fields.Boolean(required=False, description='True if there was any information from this document')
    })
class HistoryDto:
    api = Namespace('history', description='all searchs')
    
    history = api.model('history', {
        'document': fields.Integer(required=False, description='document of the patient'),
        'patient_name': fields.String(required=False, description='name of the patient'),
        'health_care_name': fields.String(required=False, description='name of the health care provider'),
        'info': fields.Boolean(required=False, description='True if there was any information from this document'),
        'service_name': fields.String(required=False, description='Web service name requested'),
        'registered_on': fields.DateTime(required=False, description='Datetime when it was registered the request/search'),
    })