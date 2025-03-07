import art
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# art.tprint("HR      Management      app")
def main_menu():
    while True:
        print(f"""{Fore.CYAN}
1. Pridėti naują darbuotoją.
2. Atvaizduoti visų darbuotojų sąrašą.
3. Ieškoti darbuotojo.
4. Atnaujinti darbuotojo informaciją.
5. Ištrinti darbuotoją.
6. Pridėti naują projektą.
7. Priskirti darbuotoją projektui.
8. Peržiūrėti darbuotojo projektus.
9. Sukurti naują departamentą.
10. Priskirti darbuotoją departamentui.
11. Peržiūrėti departamento darbuotojus.
0. Išeiti iš programos.
""")
        user_input = input("Įveskite meniu pasirinkimo numerį: ")
        if user_input == "0":
            break
        elif user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            pass
        elif user_input == "6":
            pass
        elif user_input == "7":
            pass
        elif user_input == "8":
            pass
        elif user_input == "9":
            pass
        elif user_input == "10":
            pass
        elif user_input == "11":
            pass
        else:
            print(f"{Fore.RED}Tokio pasirinkimo nėra. Bandykite dar kartą.")
