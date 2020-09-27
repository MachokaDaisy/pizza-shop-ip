import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daisy:4H@ppyfeet@localhost/pizza'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
