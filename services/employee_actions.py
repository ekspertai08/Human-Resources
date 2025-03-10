import colorama
from colorama import Fore
colorama.init(autoreset=True)

import models.employee_class as emp_cl
import models.department_class as dep_cl
import datetime
from models.DB_class import session_maker
from sqlalchemy import select

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

def show_all_employees():
    querry = select(emp_cl.Employee)
    with session_maker() as session:
        all_employees = session.execute(querry).scalars().all()
        if all_employees:
            for num, employee in enumerate(all_employees, 1):
                print(f"{num}. {employee}")
        else:
            print(f"{Fore.RED}Darbuotojų sąrašas tuščias.")

