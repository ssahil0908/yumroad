import os

class BaseConfig:
    TESTING = False
    DEBUG = False
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATION=False
    SECRET_KEY = os.getenv('SECRET_KEY', '00000abcdef')
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.mailgun.org')
    MAIL_PORT = os.getenv('MAIL_SERVER_PORT', 587)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'sahilsaini11917015@gmail.com')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', True)
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD' , '44dbb5efd5d77708886bed1bb2be5715-78f6ccbe-6d1546be')

class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_ECHO = True
    SECRET_KEY = os.getenv('SECRET_KEY', '00000abcdef')

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    WTF_CSRF_ENABLED = False
    TESTING = True
    SECRET_KEY = os.getenv('SECRET_KEY')


class ProdConfig(BaseConfig):
    SECRET_KEY = os.getenv('SECRET_KEY')

configurations = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
}