import models.department_class as dep_cl
from models.DB_class import session_maker
from sqlalchemy import select
import services.employee_actions as emp_act
import models.employee_class as emp_cl

import colorama
from colorama import Fore
colorama.init(autoreset=True)


def create_new_department():
    name = input("Įveskite naujo departamento pavadinimą: ")

    with session_maker() as session:
        department = dep_cl.Department(name=name)
        session.add(department)
        session.commit()
        print(f"{Fore.GREEN}Skyrius sukurtas sėkmingai.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_all_departments():
    querry = select(dep_cl.Department)
    with session_maker() as session:
        all_departments = session.execute(querry).scalars().all()
        if all_departments:
            print("Esami skyriai:\n")
            for num, department in enumerate(all_departments, 1):
                print(f"{num}. {department}")
        else:
            print(f"{Fore.RED}Skyrių sąrašas tuščias.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_departments_id_list():
    with session_maker() as sesion:
        id_list = sesion.execute(select(dep_cl.Department.id)).scalars().all()
        if id_list:
            return id_list
        else:
            return []
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def assign_employee_to_department():
    if get_departments_id_list() and emp_act.get_employees_id_list():
        departments_id_list = get_departments_id_list()
        show_all_departments()
        while True:
            try:
                user_input_dep = input("Įveskite skyriaus ID, kuriam norėsite priskirti darbuotoją: ")
                user_input_dep = int(user_input_dep)
                if user_input_dep in departments_id_list:
                    break
                else:
                    raise IndexError
            except ValueError:
                print(f"{Fore.RED}Įvestis nėra sveikasis skaičius. Bandykite dar kartą.")
            except IndexError:
                print(f"{Fore.RED}Tokio ID nėra. Bandykite dar kartą.")
        emp_act.show_all_employees()
        employee_id_list = emp_act.get_employees_id_list()
        while True:
            try:
                user_input_emp = input("Įveskite darbuotojo ID, kurį norėsite priskirti į pasirinktą skyrių: ")
                user_input_emp = int(user_input_emp)
                if user_input_emp in employee_id_list:
                    break
                else:
                    raise IndexError
            except ValueError:
                print(f"{Fore.RED}Įvestis nėra sveikasis skaičius. Bandykite dar kartą.")
            except IndexError:
                print(f"{Fore.RED}Tokio ID nėra. Bandykite dar kartą.")
        with session_maker() as session:
            employee = session.execute(select(emp_cl.Employee).filter_by(id=user_input_emp)).scalar_one_or_none()
            department = session.execute(select(dep_cl.Department).filter_by(id=user_input_dep)).scalar_one_or_none()
            employee.department_id = department.id
            session.commit()
            print(f"{Fore.GREEN}Darbuotojas sėkmingai priskirtas skyriui.")
    else:
        print(f"{Fore.RED}Darbuotojų arba skyrių sąrašas tuščias.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_department_employees():
    if get_departments_id_list():
        departments_id_list = get_departments_id_list()
        show_all_departments()
        while True:
            try:
                user_input_dep = input("Įveskite skyriaus ID, kurio darbuotojus norėsite pamatyti: ")
                user_input_dep = int(user_input_dep)
                if user_input_dep in departments_id_list:
                    break
                else:
                    raise IndexError
            except ValueError:
                print(f"{Fore.RED}Įvestis nėra sveikasis skaičius. Bandykite dar kartą.")
            except IndexError:
                print(f"{Fore.RED}Tokio ID nėra. Bandykite dar kartą.")
        with session_maker() as session:
            querry1 = select(dep_cl.Department).filter_by(id = user_input_dep)
            department = session.execute(querry1).scalar_one_or_none()
            querry2 = select(emp_cl.Employee).filter_by(department_id = user_input_dep)
            employees = session.execute(querry2).scalars().all()
            print(f"Skyriuje: {department} dirba:")
            for employee in employees:
                print(employee)
