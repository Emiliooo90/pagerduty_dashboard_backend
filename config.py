import os


class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql://root:emilio12345678.@db:3306/pagerdutydatabase"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SECRET_KEY = os.getenv('SECRET_KEY')
    PAGERDUTY_API_KEY = os.getenv('PAGERDUTY_API_KEY')