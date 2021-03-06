import os
from dotenv import load_dotenv

load_dotenv(f"{os.path.dirname(os.path.realpath(__file__))}/.env")


class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{os.path.dirname(os.path.realpath(__file__))}/app.db"
    SECRET_KEY = 'vZ9YVje1aU'
