from run import app
from models import db, Paciente, CasoDengue, Ubicacion

# Borrar y crear todas las tablas
with app.app_context():
    db.drop_all()
    db.create_all()

    # Crear datos de ejemplo (opcional)
    paciente1 = Paciente(nombre="Juan Pérez", edad=30, direccion="Calle Falsa 123", barrio="Centro")
    paciente2 = Paciente(nombre="María García", edad=25, direccion="Avenida Siempre Viva 742", barrio="Sur")

    db.session.add(paciente1)
    db.session.add(paciente2)
    db.session.commit()

    caso1 = CasoDengue(paciente_id=paciente1.id, tipo="A")
    caso2 = CasoDengue(paciente_id=paciente2.id, tipo="B")

    db.session.add(caso1)
    db.session.add(caso2)
    db.session.commit()

    print("Base de datos reiniciada y datos de ejemplo creados.")
