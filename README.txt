· Tikslas

Sukurti Python programą, kuri leistų valdyti darbuotojų duomenis naudojant SQLAlchemy ORM. Programa turi palaikyti darbuotojų registravimą, atnaujinimą, peržiūrą ir šalinimą. Taip pat turi būti įgyvendintas daug-daug (Many-to-Many) ryšys tarp darbuotojų ir projektų bei vienas-daug (One-to-Many) ryšys tarp darbuotojų ir departamentų.

---

· Reikalavimai

· 1. Pagrindinis meniu

Programa turi pateikti vartotojui pasirinkimus:

1. Pridėti naują darbuotoją

2. Atvaizduoti visų darbuotojų sąrašą

3. Ieškoti darbuotojo

4. Atnaujinti darbuotojo informaciją

5. Ištrinti darbuotoją

6. Pridėti naują projektą

7. Priskirti darbuotoją projektui

8. Peržiūrėti darbuotojo projektus

9. Sukurti naują departamentą

10. Priskirti darbuotoją departamentui

11. Peržiūrėti departamento darbuotojus

12. Išeiti iš programos

Meniu turi būti realizuotas naudojant ciklą, kad vartotojas galėtų atlikti kelis veiksmus iki programos pabaigos.

---

· 2. Duomenų bazės schema

· Darbuotojas (employees)

· id – pirminis raktas

· vardas – privalomas

· pavardė – privalomas

· gimimo_data – privalomas

· pareigos – privalomas

· atlyginimas – privalomas

· pradžios_data – nustatoma automatiškai

· departamentas_id – išorinis raktas į departamentus

· Projektas (projects)

· id – pirminis raktas

· pavadinimas – privalomas

· aprašymas – privalomas

· Darbuotojo-Projekto asociacinė lentelė (employee_project)

· id – pirminis raktas

· darbuotojas_id – išorinis raktas į darbuotojus

· projektas_id – išorinis raktas į projektus

· role_projekte – papildomas laukas (neprivalomas)

· Departamentas (departments)

· id – pirminis raktas

· pavadinimas – privalomas

· vadovas_id – išorinis raktas į darbuotojus (neprivalomas)

---

· 3. Funkcionalumas

· Darbuotojo valdymas

· Sukurti naujo darbuotojo registraciją.

· Peržiūrėti visų darbuotojų sąrašą.

· Ieškoti darbuotojo pagal vardą, pavardę arba ID.

· Atnaujinti darbuotojo informaciją (pareigas ir atlyginimą).

· Ištrinti darbuotoją (jei turi susietų projektų ar departamento – tai tinkamai apdoroti).

· Projektų valdymas

· Registruoti naują projektą.

· Priskirti darbuotoją projektui (Many-to-Many ryšys).

· Peržiūrėti, kuriuose projektuose dalyvauja konkretus darbuotojas.

· Departamentų valdymas

· Kurti naują departamentą.

· Priskirti darbuotoją departamentui (One-to-Many ryšys).

· Peržiūrėti darbuotojus, priklausančius konkrečiam departamentui.