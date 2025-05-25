from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    barrio = db.Column(db.String(100), nullable=False)

class CasoDengue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # A, B, C
    fecha_diagnostico = db.Column(db.DateTime, default=datetime.utcnow)
    paciente = db.relationship('Paciente', backref=db.backref('casos', lazy=True))

class Ubicacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barrio = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    caso_id = db.Column(db.Integer, db.ForeignKey('caso_dengue.id'), nullable=False)
