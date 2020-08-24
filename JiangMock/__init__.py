from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import *

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = sessionmaker(engine)()

from JiangMock import views, models