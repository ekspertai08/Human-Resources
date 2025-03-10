import colorama
from colorama import Fore
colorama.init(autoreset=True)

import models.employee_class as emp_cl
import models.department_class as dep_cl
import datetime
from models.DB_class import session_maker
from sqlalchemy import select

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_new_employee():
    name = input("Įveskite naujo darbuotojo vardą: ")
    last_name = input("Įveskite naujo darbuotojo pavardę: ")
    while True:
        try:
            dob = input("Įveskite naujo darbuotojo gimimo datą (formatu YYYY-MM-DD): ")
            dob = datetime.datetime.strptime(dob, "%Y-%m-%d")
            break
        except ValueError:
            print(f"{Fore.RED}Data įvesta netinkamu formatu. Bandykite dar kartą.")
    position = input("Įveskite naujo darbuotojo pareigas: ")
    while True:
        try:
            salary = input("Įveskite naujo darbuotojo atlyginimą: ")
            salary = int(salary)
            break
        except ValueError:
            print(f"{Fore.RED}Atlyginimas įvestas netinkamu formatu, įveskite tik sveikuosius skaičius. Bandykite dar kartą.")

    with session_maker() as session:
        new_employee = emp_cl.Employee(name=name, last_name=last_name, dob=dob, position=position, salary=salary)
        session.add(new_employee)
        session.commit()
        print(f"{Fore.GREEN}\nDarbuotojas sukurtas ir išsaugotas sėkmingai.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_all_employees():
    querry = select(emp_cl.Employee)
    with session_maker() as session:
        all_employees = session.execute(querry).scalars().all()
        if all_employees:
            print("Esami darbuotojai:\n")
            for num, employee in enumerate(all_employees, 1):
                print(f"{num}. {employee}")
        else:
            print(f"{Fore.RED}Darbuotojų sąrašas tuščias.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_employees_id_list():
    with session_maker() as sesion:
        id_list = sesion.execute(select(emp_cl.Employee.id)).scalars().all()
        if id_list:
            return id_list
        else:
            return []
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def search_for_employee():
    # Ieškoti darbuotojo pagal vardą, pavardę arba ID.
    if get_employees_id_list():
        print("""
    Galimi paieškos parametrai:
    1. Vardas
    2. Pavardė
    3. ID
              """)
        user_input = input("Įveskite pagal kokį parametrą atliksite paiešką: ")
        if user_input == "1":
            user_input = input("Įveskite ieškomą frazę ar dalį frazės: ")
            with session_maker() as session:
                querry = select(emp_cl.Employee).where(emp_cl.Employee.name.like(f'%{user_input.capitalize()}%'),emp_cl.Employee.name.like(f'%{user_input.lower()}%'),emp_cl.Employee.name.like(f'%{user_input.title()}%'))
                employees = session.execute(querry).scalars().all()
                if employees:
                    print("Rasta:\n")
                    for employee in employees:
                        print(employee)
                else:
                    print(f"{Fore.RED}Nieko nerasta.")

        elif user_input == "2":
            user_input = input("Įveskite ieškomą frazę ar dalį frazės: ")
            with session_maker() as session:
                querry = select(emp_cl.Employee).where(emp_cl.Employee.last_name.like(f'%{user_input.capitalize()}%'),emp_cl.Employee.last_name.like(f'%{user_input.lower()}%'),emp_cl.Employee.last_name.like(f'%{user_input.title()}%'))
                employees = session.execute(querry).scalars().all()
                if employees:
                    for employee in employees:
                        print(employee)
                else:
                    print(f"{Fore.RED}Nieko nerasta.")
        elif user_input == "3":
            while True:
                try:
                    user_input = input("Įveskite ieškomą ID numerį: ")
                    user_input = int(user_input)
                    break
                except ValueError:
                    print(f"{Fore.RED}ID įvesti galima tik sveikaisiais skaičiais. Bandykite dar kartą.")
            with session_maker() as session:
                querry = select(emp_cl.Employee).filter_by(id=user_input)
                employees = session.execute(querry).scalars().all()
                if employees:
                    for employee in employees:
                        print(f"{employee}")
                else:
                    print(f"{Fore.RED}Nieko nerasta.")
    else:
        print(f"{Fore.RED}Darbuotojų sąrašas tuščias.")
                
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_employee():
    employee_id_list = get_employees_id_list()
    show_all_employees()
    if len(employee_id_list) > 0:
        while True:
            try:
                user_input = input("Įveskite norimo redaguoto darbuotojo ID: ")
                user_input = int(user_input)
                if user_input in employee_id_list:
                    break
                else:     
                    raise IndexError
            except IndexError:
                print(f"{Fore.RED}Tokio darbuotojo ID nėra. Bandykite dar kartą.")
            except ValueError:
                print(f"{Fore.RED}Įvesties klaida. Įveskite tik sveikuosius skaičius. Bandykite dar kartą.")
        with session_maker() as sesion:
            querry = select(emp_cl.Employee).filter_by(id=user_input)
            upd_employee = sesion.execute(querry).scalar_one()
            column_names = [column.name for column in emp_cl.Employee.__table__.columns]
            for num, i in enumerate(column_names):
                if num == 0:
                    continue
                print(f"{num}. {i}")
            while True:
                user_input = input("Pasirinkite norimo pakeisti parametro numerį: ")
                try:
                    user_input = int(user_input)
                    if user_input-1 in range(0, len(column_names)):
                        break
                    else:
                        raise IndexError
                except ValueError:
                    print(f"{Fore.RED}Įvestis nėra sveikasis skaičius. Bandykite dar kartą.")
                except IndexError:
                    print(f"{Fore.RED}Tokio parametro numerio nėra. Bandykite dar kartą.")
            if user_input == 3:
                while True:
                    try:
                        user_new_value = input("Įveskite naują darbuotojo gimimo datą (formatu YYYY-MM-DD): ")
                        user_new_value = datetime.datetime.strptime(user_new_value, '%Y-%m-%d')
                        break
                    except ValueError:
                        print(f"{Fore.RED}Data įvesta netinkamu formatu. Bandykite dar kartą.")
            elif user_input == 5:
                    while True:
                        try:
                            user_new_value = input("Įveskite naujo darbuotojo atlyginimą: ")
                            user_new_value = int(user_new_value)
                            break
                        except ValueError:
                            print(f"{Fore.RED}Atlyginimo įvestis neteisinga. Įveskite tik sveikuosius skaičius. Bandykite dar kartą.")
            else:
                user_new_value = input("Įveskite naują reikšmę: ")
                
            column_name = column_names[user_input]
            setattr(upd_employee, column_name, user_new_value)
            sesion.commit()
            print(f"{Fore.GREEN}Darbuotojas atnaujintas sėkmingai.")
            
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def delete_employee():
    show_all_employees()
    employee_id_list = get_employees_id_list()
    if employee_id_list:
        while True:
            try:
                user_input = input("Įveskite norimo ištrinti darbuotojo ID arba norint nutraukti įveskite 'q': ")
                if user_input == 'q':
                    break
                user_input = int(user_input)
                if user_input in employee_id_list:
                    with session_maker() as session:
                        querry = select(emp_cl.Employee).filter_by(id=user_input)
                        employee = session.execute(querry).scalar_one()
                        if employee:
                            session.delete(employee)
                            session.commit()
                            print(f"{Fore.GREEN}Darbuotojas ištrintas sėkmingai.")
                            break
                else:
                    print(f"{Fore.RED}Darbuotojo su tokiu ID nėra.")
            except ValueError:
                print(f"{Fore.RED}ID įvestis galima tik sveikaisiais skaičiais. Bandykite dar kartą.\n")

