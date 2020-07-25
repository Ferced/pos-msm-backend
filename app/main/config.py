import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pos_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pos_main.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
ioma_config = dict(
    url = "http://sistemasl.ioma.gba.gov.ar/sistemas/consulta_padron_afiliados/buscadorpordocumento.php"
)

spin_config = dict(
    user_spin =  'sss1754',
    password_spin = 'Larcade04',
    url = 'https://seguro.sssalud.gob.ar/indexss.php?opc=bus650&user=HPGD&cat=consultas'
)

puco_config = dict(
    url="http://170.150.155.102/nacer/personas_puco_con_documentos.php"
)

puco_sumar_config = dict(
    url="http://170.150.155.102/nacer/personas_inscriptas_hist_con_documentos.php"
)

pami_config = dict(
    url = "https://prestadores.pami.org.ar/result.php?c=6-2-2",
    url_base = "https://prestadores.pami.org.ar/"
)

key = Config.SECRET_KEY
