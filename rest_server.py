from flask import Flask, render_template, Blueprint

def REST_blueprint(): 
    API = Blueprint('REST_API', __name__, template_folder = "templates")

    @API.route("/")
    def index(): 
	return render_template("index.html")

    return API


    

