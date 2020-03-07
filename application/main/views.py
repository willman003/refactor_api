from . import main
from ..api_handler.handler import *
from flask import render_template, redirect, url_for

@main.route('/',methods=['GET','POST'])
def index():
    answer = api_get_users()
    
    return answer