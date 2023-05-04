"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cha0sq2k728r886jl110-a.oregon-postgres.render.com",
        database="todoapp_0sd8",
        user="todoapp_0sd8_user",
        password="Kkd60S6xlPDk4XW6WxbMzSr4oXlc9KZ5")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
