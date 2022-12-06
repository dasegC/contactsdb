from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contacts import Contact
from utils.db import db

################################################################################################

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def index():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


################################################################################################


@contacts.route("/new", methods=["POST"])
def add_contact():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    email = request.form["email"]
    phone = request.form["phone"]
    img = request.form["img"]

    new_contact = Contact(firstname, lastname, email, phone, img)

    db.session.add(new_contact)  # Agrega el contacto a la db
    db.session.commit()  # Acaba con la conexión a la db

    flash('Contacto Añadido Correctamente!')

    return redirect(url_for("contacts.index"))


################################################################################################


@contacts.route("/about")
def about():
    return render_template('about.html')


################################################################################################


@contacts.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    contact = Contact.query.get(id)  # Consulta el contacto
    if request.method == "POST":
        contact.firstname = request.form["firstname"]
        contact.lastname = request.form["lastname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]
        contact.img = request.form["img"]

        db.session.commit()

        flash('Contacto Actualizado Correctamente!')

        return redirect(url_for("contacts.index"))

    return render_template("update.html", contact=contact)


################################################################################################


@contacts.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(
        id
    )  # Obtiene y guarda el contacto por id en la variable
    db.session.delete(contact)  # Elimina el contacto
    db.session.commit()
    
    flash('Contacto Borrado Correctamente!')
    
    return redirect(url_for("contacts.index"))
