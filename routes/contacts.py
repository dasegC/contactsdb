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
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    new_contact = Contact(fullname, email, phone)

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
        contact.fullname = request.form["fullname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]

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
