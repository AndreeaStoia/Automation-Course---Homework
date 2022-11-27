'''Pentru toate clasele, creați cel puțin 2 obiecte cu valori diferite și apelați toate metodele clasei.

1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()'''

class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Raza cercului este {self.raza} iar culoarea cercului este {self.culoare}.")

    def aria(self):
        PI=3.14
        aria= PI * self.raza ** 2
        return aria

    def diametru(self):
        diametru = self.raza * 2
        return diametru

    def circumferinta(self):
        PI=3.14
        circumferinta = 2 * self.raza * PI
        return circumferinta

a= Cerc(5, "rosu")
a.descrie_cerc()
print(f"Aria cercului este {a.aria()}.")
print(f"Diametrul cercului este {a.diametru()}.")
print(f"Circumferinta cercului este {a.circumferinta()}.")

b=Cerc(10, "roz")
b.descrie_cerc()
print(f"Aria cercului este {b.aria()}.")
print(f"Diametrul cercului este {b.diametru()}.")
print(f"Circumferinta cercului este {b.circumferinta()}.")

'''2. Clasa Dreptunghi
Atribute: lungime, latime, culoare. Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. 
Puteti verifica schimbarea culorii prin apelarea metodei descrie().'''

class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime=lungime
        self.latime=latime
        self.culoare=culoare

    def descrie_dreptunghi(self):
        print(f"Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}.")

    def arie_dreptunghi(self):
        aria = self.lungime * self.latime
        return aria

    def perimetru_dreptunghi(self):
        perimetru = 2*(self.lungime + self.latime)
        return perimetru
    def schimbă_culoarea(self, noua_culoare):
        self.culoare = noua_culoare

c = Dreptunghi(2,3,"albastru")
c.descrie_dreptunghi()
print(f"Aria dreptunghiului este {c.arie_dreptunghi()}.")
print(f"Perimetrul dreptunghiului este {c.perimetru_dreptunghi()}.")
c.schimbă_culoarea("mov")
c.descrie_dreptunghi()

d = Dreptunghi(10,2,"galben")
d.descrie_dreptunghi()
print(f"Aria dreptunghiului este {d.arie_dreptunghi()}.")
print(f"Perimetrul dreptunghiului este {d.perimetru_dreptunghi()}.")
d.schimbă_culoarea("gri")
d.descrie_dreptunghi()

'''3. Clasa Angajat
Atribute: nume, prenume, salariu. Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)'''

class Angajat:
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie_angajat(self):
        print(f"Angajatul {self.nume} {self.prenume} are salariul de {self.salariu} RON.")

    def nume_complet(self):
        nume_complet = print(f"{self.nume} {self.prenume}.")
        return nume_complet

    def salariu_lunar(self):
        salariu_lunar = self.salariu
        return salariu_lunar

    def salariu_anual(self):
        salariu_anual = self.salariu_lunar() * 12
        return salariu_anual

    def marire_salariu(self, procent):
        self.procent = procent/100
        marire_salariu = self.salariu_lunar() * self.procent
        salariu_lunar_nou = self.salariu_lunar() + marire_salariu
        salariu_anual_nou = salariu_lunar_nou*12
        print(f"Noul salariu lunar este de {salariu_lunar_nou}.")
        print(f"Noul salariu anual este de {salariu_anual_nou}.")

e = Angajat("Maria", "Ionescu", 10000)
e.descrie_angajat()
e.nume_complet()
print(e.salariu_lunar())
print(e.salariu_anual())
e.marire_salariu(5)

f = Angajat("Ion", "Gheorghe", 3000)
f.descrie_angajat()
f.nume_complet()
print(f.salariu_lunar())
print(f.salariu_anual())
f.marire_salariu(10)

'''4.Clasa Cont. Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)'''

class Cont:
    IBAN = None
    titular_cont = None
    sold = 0

    def __init__(self, IBAN, titular_cont,sold):
        self.IBAN = IBAN
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.IBAN} suma de {self.sold} lei.")

    def debitare_cont(self, suma):
        self.sold -= suma
        print(f"Dupa debitarea cu {suma} lei, soldul curent este: {self.sold} lei.")

    def creditare_cont(self, suma):
        self.sold +=suma
        print(f"Dupa creditarea cu {suma} lei, soldul curent este: {self.sold} lei.")

g = Cont("ROXXXXXXXXXXXXXXXXXX","Maria Ionescu", 1000)
g.afisare_sold()
g.debitare_cont(200)
g.creditare_cont(300)

h = Cont("ROXXXXXXXXXXXXXXXXXX","Gigel Popescu", 50)
h.afisare_sold()
h.debitare_cont(1000)
h.creditare_cont(1500)

'''1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/'''

from datetime import date
from tabulate import tabulate

class Factura:
    SERIA = "SR12345"
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self,nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        print(f'Factura seria: {self.SERIA} numar: {self.numar}')
        print(f'Data: {date.today()}')
        data = [["Produs","Cantitate","Pret bucata","Total"], [self.nume_produs, self.cantitate, self.pret_buc, self.cantitate*self.pret_buc], ["Telefon", "07", 700, 49000]]
        print(tabulate(data, headers='firstrow',tablefmt='fancy_grid'))

factura1 = Factura(123, "Rochie seara", 3, 250)
factura1.genereaza_factura()
factura1.schimba_nume_produs("Rochie mireasa")
factura1.schimba_cantitatea(10)
factura1.schimba_pretul(2000)
factura1.genereaza_factura()
print(f"---------------------------")
factura2 = Factura(456, "Mobila hol", 5, 1500)
factura2.genereaza_factura()
factura2.schimba_nume_produs("Mobila gradina")
factura2.schimba_cantitatea(2)
factura2.schimba_pretul(600)
factura2.genereaza_factura()

'''2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0'''

class Masina:
    marca = "Dacia"
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = {"alb", "negru", "rosu", "albastru", "verde"}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie_masina(self):
        print(f"Masina {self.marca} model {self.model}, culoare {self.culoare}, cu viteza maxima de {self.viteza_maxima} km/ are o viteza actuala de {self.viteza_actuala} km/h. In prezent este inmatriculata: {self.inmatriculata}.")
    def schimba_inmatriculare(self):
        self.inmatriculata = True
        print(f"Masina este acum inmatriculata: {self.inmatriculata}.")
    def schimba_culoare(self,culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f"Acum culoarea masinii este {self.culoare}.")
        else:
            print(f"Eroare: culoare indisponibila. Alegeti una dintre culorile disponibile.")
            culoare=input("Introduceti noua culoare: ")
    def accelereaza(self,viteza):
        if viteza <0:
            print("Eroare: Viteza insuficienta.")
        elif viteza + self.viteza_actuala > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            print(f"Ati atins viteza maxima.")
        else:
            self.viteza_actuala += viteza
            print(f"Viteza actuala este de {self.viteza_actuala} km/h.")
    def franeaza(self):
        self.viteza_actuala = 0
        print(f"Masina s-a oprit.")

masina1 = Masina(1310,120)
masina1.descrie_masina()
masina1.schimba_inmatriculare()
masina1.schimba_culoare("albastru")
masina1.accelereaza(150)
masina1.franeaza()
print("--------------------------------")
masina2 = Masina("Logan",240)
masina2.descrie_masina()
masina2.schimba_inmatriculare()
masina2.schimba_culoare("roz")
masina2.accelereaza(-50)
masina2.franeaza()

'''3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict'''

class TodoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.nume = input("Introdu nume task: ")
        self.descriere = input("Introdu descriere task: ")
        self.todo.update({nume: descriere})

class TodoList:
    todo = {}

    def adauga_task(self,nume,descriere):
        self.todo[nume]=descriere

    def finalizeaza_task(self,nume):
        self.todo.pop(nume)

    def afiseaza_todo_list(self):
        print(self.todo.keys())

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo.keys():
            alternative = input("Taskul nu e in todo list, doriti sa-l adaugam: ")
            if alternative == "da":
                detalii = input("Introduceti detaliile taskului: ")
                self.adauga_task(nume_task, detalii)
            else:
                print("La revedere!")
        else:
            print(f"Detalii suplimentare: {self.todo[nume_task]}")

todo1= TodoList()
todo1.adauga_task("Mancare","pregateste mic dejun")
todo1.adauga_task("Gradina","uda florile")
todo1.adauga_task("Animale","hraneste cainele si pisica")
print(todo1.todo)
todo1.finalizeaza_task("Mancare")
print(todo1.todo)
todo1.afiseaza_todo_list()
todo1.afiseaza_detalii_suplimentare("Gradina")
todo1.afiseaza_detalii_suplimentare("Masina")
print(todo1.todo)