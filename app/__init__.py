"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cg99tjm4dad5p6psm8d0-a.oregon-postgres.render.com",
        database="todo_demo3_dxh8",
        user="todo_demo3_dxh8_user",
        password="fCzt50gnSzKNwbip3p55AiIcGPc1aygA")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
