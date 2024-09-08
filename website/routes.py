from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .data import *
from .models import *
from . import db
import os

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return render_template("landing.html")

@routes.route("/about")
def about():
    return render_template("about.html")

@routes.route("/dashboard")
@login_required
def dashboard():
    farms = Farm.query.filter_by(owner_id=current_user.id).all()
    print(farms)
    return render_template("dashboard.html", user=current_user, farms=farms)

@routes.route("/new", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        address = request.form.get("address")
        state = request.form.get("state")
        district = request.form.get("district")
        area =  request.form.get("area")
        area_unit =  request.form.get("area-unit")

        print(area)
        print(area_unit)

        print(convert_to_hectares(area, area_unit))

        new = Farm(address=address, soil="", state=state, district=district, land_area=round(convert_to_hectares(area, area_unit)), owner_id=current_user.id)
        db.session.add(new)
        db.session.commit()
        print("farm created")
        return redirect("/dashboard")

    return render_template("new.html", user=current_user, districts_of_india=districts_of_india, states_and_uts_of_india=states_and_uts_of_india)


@routes.route("/farm/<id>")
@login_required
def farm(id):
    farm = Farm.query.get(id)
    try:
        crops = soilPlants[farm.soil]
    except:
        crops=[]
    try:
        crop = Plant.query.filter_by(farm_id=id).first()
    except:
        crop = None

    if farm.owner_id == current_user.id:
        return render_template("farm.html", farm=farm, suggested=suggest_soils(farm.state)[0], total=suggest_soils(farm.state)[1], crops=crops, crop=crop, costing=costing, processtime=processtime, sum=sum, round=round)
    else:
        return redirect("/")
    
@routes.route("/farm/<id>/set-soil", methods=["POST"])
@login_required
def setsoil(id):
    farm = Farm.query.get(id)
    farm.soil = request.form.get("soil")
    db.session.commit()
    return redirect("/farm/"+id)

@routes.route("/farm/<id>/set-plant", methods=["POST"])
@login_required
def setplant(id):
    plant = Plant(farm_id=id, plant_name=request.form.get("crop"))
    db.session.add(plant)
    db.session.commit()
    return redirect("/farm/"+id)

@routes.route("/delete/<id>")
@login_required
def delete(id):
    farm = Farm.query.get(id)
    db.session.delete(farm)
    db.session.commit()
    return redirect("/dashboard")

@routes.route("/assist")
@login_required
def assist():
    return render_template("assist.html")