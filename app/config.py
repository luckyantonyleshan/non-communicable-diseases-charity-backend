import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False