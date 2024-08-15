import os


class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql://root:{os.getenv('DB_PASSWORD')}@db:3306/{os.getenv('DB_DATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SECRET_KEY = os.getenv('SECRET_KEY')
    PAGERDUTY_API_KEY = os.getenv('PAGERDUTY_API_KEY')