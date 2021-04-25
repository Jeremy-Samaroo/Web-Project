from flask import Blueprint, redirect, render_template, request

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('index.html')

@api_views.route('/homepage', methods=['GET'])
def home():
    return render_template('homepage.html')

@api_views.route('/list', methods=['GET'])
def list():
    return render_template('list.html')

@api_views.route('/recipes', methods=['GET'])
def recipes():
    return render_template('recipes.html')
