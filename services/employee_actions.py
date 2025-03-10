import models.employee_class as emp_cl
import models.department_class as dep_cl
import datetime
from models.DB_class import session_maker

def create_new_employee():
    name = input("Įveskite naujo darbuotojo vardą: ")
    last_name = input("Įveskite naujo darbuotojo pavardę: ")
    dob = input("Įveskite naujo darbuotojo gimimo datą (formatu YYYY-MM-DD): ")
    dob = datetime.datetime.strptime(dob, "%Y-%m-%d")
    position = input("Įveskite naujo darbuotojo pareigas: ")
    salary = input("Įveskite naujo darbuotojo atlyginimą: ")
    salary = int(salary)

    with session_maker() as session:
        new_employee = emp_cl.Employee(name=name, last_name=last_name, dob=dob, position=position, salary=salary)
        session.add(new_employee)
        session.commit()