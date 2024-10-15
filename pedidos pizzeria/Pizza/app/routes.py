from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Paciente, CasoDengue, Ubicacion

main = Blueprint('main', __name__)

@main.route('/')
def index():
    casos = CasoDengue.query.all()
    return render_template('index.html', casos=casos)

@main.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        barrio = request.form['barrio']
        tipo = request.form['tipo']
        
        paciente = Paciente(nombre=nombre, edad=edad, direccion=direccion, barrio=barrio)
        db.session.add(paciente)
        db.session.commit()

        caso = CasoDengue(paciente_id=paciente.id, tipo=tipo)
        db.session.add(caso)
        db.session.commit()

        return redirect(url_for('main.index'))
    
    return render_template('registrar.html')
