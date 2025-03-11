import colorama
from colorama import Fore
colorama.init(autoreset=True)

import models.project_class as pro_cl
import models.employee_class as emp_cl
import models.employee_project_class as emp_pro_cl
from models.DB_class import session_maker
from sqlalchemy import select
from services.employee_actions import show_all_employees, get_employees_id_list

def add_new_project():
    name = input("Įveskite projekto pavadinimą: ")
    description = input("Įveskite projekto aprašymą: ")
    with session_maker() as session:
        new_project = pro_cl.Project(name, description)
        session.add(new_project)
        session.commit()
        print(f"{Fore.GREEN}\nProjektas pridėtas ir išsaugotas sėkmingai.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_all_projects():
    with session_maker() as session:
        querry = select(pro_cl.Project)
        projects = session.execute(querry).scalars().all()
        if projects:
            for project in projects:
                print(project)
        else:
            print(f"{Fore.RED}Projektų sąrašas tuščias.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def get_projects_id_list():
    with session_maker() as session:
        id_list = session.execute(select(pro_cl.Project.id)).scalars().all()
        if id_list:
            return id_list
        else:
            return []

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def assign_employee_to_project():
    if get_projects_id_list() and get_employees_id_list():
        projects_id_list = get_projects_id_list()
        employees_id_list = get_employees_id_list()
        show_all_employees()
        while True:
            try:
                user_input_emp = input("Įveskite darbuotojo ID, kurį norite priskirti į projektą: ")
                user_input_emp = int(user_input_emp)
                if user_input_emp in employees_id_list:
                    break
                else:
                    raise IndexError
            except ValueError:
                print(f"{Fore.RED}Įvestis galima tik sveikaisiais skaičiais. Bandykite dar kartą.")
            except IndexError:
                print(f"{Fore.RED}Darbuotojo tokiu indeksu nėra. Bandykite dar kartą.")
        show_all_projects()
        while True:
            try:
                user_input_pro = input("Įveskite projekto ID, į kurį norite priskirti darbuotoją: ")
                user_input_emp = int(user_input_emp)
                if user_input_emp in projects_id_list:
                    break
                else:
                    raise IndexError
            except ValueError:
                print(f"{Fore.RED}Įvestis galima tik sveikaisiais skaičiais. Bandykite dar kartą.")
            except IndexError:
                print(f"{Fore.RED}Projekto tokiu indeksu nėra. Bandykite dar kartą.")
        with session_maker() as session:
            querry = select(emp_cl.Employee).filter_by(id=user_input_emp)
            employee = session.execute(querry).scalar_one()
            querry = select(pro_cl.Project).filter_by(id=user_input_pro)
            project = session.execute(querry).scalar_one()
            new_employee_project = emp_pro_cl.Employee_Project(employee_id=employee.id, project_id=project.id)
            session.add(new_employee_project)
            session.commit()
            print(f"{Fore.GREEN}Projektas priskirtas sėkmingai.")
    else:
        print(f"{Fore.RED}Darbuotojų arba projektų sąrašas tuščias.")
            
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_emloyee_projects():
    if get_employees_id_list() and get_projects_id_list():
        show_all_employees()
        while True:
            try:
                user_input_emp = input("Įveskite darbuotojo ID, kurio projektus norite pamatyti: ")
                user_input_emp = int(user_input_emp)
                if user_input_emp in get_employees_id_list():
                    break
                else:
                    raise IndexError
            except ValueError:
                print(f"{Fore.RED}Įvestis galima tik sveikaisiais skaičiais. Bandykite dar kartą.")
            except IndexError:
                print(f"{Fore.RED}Darbuotojo tokiu indeksu nėra. Bandykite dar kartą.")
        with session_maker() as session:
            employee = session.execute(select(emp_cl.Employee).filter_by(id=user_input_emp)).scalar_one_or_none()
            if employee:
                projects = [assoc.project for assoc in employee.project_associations]
                if projects:
                    print("Darbuotojo projektai:")
                    for project in projects:
                        print(project)
                else:
                    print(f"{Fore.RED}Darbuotojas neturi priskirtų projektų.")
            
    else:
        print(f"{Fore.RED}Darbuotojų sąrašas arba projektų sąrašas tuščias.")
