from utils.db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    img = db.Column(db.String(4000))

    def __init__(self, firstname, lastname, email, phone, img):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.img = img
