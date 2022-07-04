"""root of gwee web app"""
import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
load_dotenv()
app = Flask(__name__)
user_name = os.environ.get("DATABASE_USERNAME")
password = os.environ.get("DATABASE_PASSWORD")
path = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql+psycopg2://{user_name}:{password}@{path}'
app.config["SECRET_KEY"] = os.environ.get("GWEE_DATABASE_KEY","")

# conn_string = "host='localhost' dbname='review_posts' user='postgres' password='1337514' port=5432"
# conn = psycopg2.connect(conn_string)

db = SQLAlchemy(app)