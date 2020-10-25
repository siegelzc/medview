from flask import render_template
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask import Flask, render_template, request

from . import app
from .config import institution_types, provider_types

@app.route('/', methods=['GET'])
def home_page():
    return render_template('home_page.html', health_institutions=institution_types, insurance_providers=provider_types)
@app.route('/about_page', methods=['GET'])
def about_page():
    return render_template('about_us.html')
@app.route('/home_page', methods=['GET'])
def home_back():
    return render_template('home_page.html', health_institutions=institution_types, insurance_providers=provider_types)
