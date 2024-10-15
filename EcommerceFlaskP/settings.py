from flask import Flask, flash, render_template, redirect, make_response, request, url_for, session, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, IntegerField
from wtforms.validators import InputRequired, Email, Length, DataRequired
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required, current_user
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xdf\xec\xf0e\x96@h\xa8\xc9\xf9\xbe\x0b\xac^\x0ci[\x17\xa6\xb8/H<\x94'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:aa09@localhost/geek_text"
admin = Admin(app, name='geek_text', template_mode='bootstrap3')



