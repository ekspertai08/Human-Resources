import models.department_class as dep_cl
from models.DB_class import session_maker

def create_new_department():
    name = input("Įveskite naujo departamento pavadinimą: ")
    with session_maker() as session:
        department = dep_cl.Department(name)
        session.add(department)
        session.commit()