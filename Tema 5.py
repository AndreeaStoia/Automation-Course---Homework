'''1. Funcție care să calculeze și să returneze suma a două numere'''

def suma_numere(n1, n2 ):
    sum=n1+n2
    return sum

n1 = int(input("Introduceti un numar:"))
n2 = int(input("Introduceti un alt numar:"))
print(f'Suma numerelor {n1} si {n2} este {suma_numere(n1,n2)}.')

'''2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar.'''
def true_or_false (numar):
    if numar%2==0:
        message = "TRUE"
    else:
        message = "FALSE"
    return message
numar = int(input("Introduceti un numar: "))
print(f"Numarul {numar} este par: {true_or_false(numar)}.")

'''3. Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)'''

def nume_complet(nume, prenume,nume_mijlociu):
    lungime = len(nume) + len(prenume) + len(nume_mijlociu)
    return lungime

nume = input("Introduceti nume:")
prenume = input("Introduceti prenume: ")
nume_mijlociu = input("Introduceti nume mijlociu:")
print(f"Numarul de caractere al numelui {nume} {prenume} {nume_mijlociu} este {nume_complet(nume, prenume, nume_mijlociu)}".)

'''4. Funcție care returnează aria dreptunghiului.'''
def aria_dreptunghiului (lungime, latime):
    aria = lungime*latime
    return aria

lungime = int(input("Introduceti lungime dreptunghi: "))
latime = int(input("Introduceti latime dreptunghi: "))
print(f"Aria dreptunghiului cu lungimea de {lungime} m si latimea de {latime} m este {aria_dreptunghiului(lungime, latime)} m.")

'''5. Funcție care returnează aria cercului'''
def aria_cercului (raza):
    PI = 3.14
    aria = PI*(raza**2)
    return aria

raza = int(input("Introduceti raza cerc: "))
print(f"Aria cercului cu raza de {raza} m este de {aria_cercului(raza)} m.")

'''6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.'''

def cauta_caracter (caracter, string):
    if caracter in string:
        message = "True"
    else:
        message = "False"
    return message

string = input("Introduceti un string:")
caracter = input("Introduceti un caracter:")
print(f"Caracterul introdus {caracter} se afla in stringul {string}: {cauta_caracter(caracter, string)}.")

'''7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case este y'''

def numar_caractere(caracter, string):
    suma_lower = sum (1 for caracter in string if caracter.islower())
    suma_upper = sum (1 for caracter in string if caracter.isupper())
    print(f"Nr de caractere lower case este {suma_lower}")
    print((f"Nr de caractere upper case este {suma_upper}"))

string = input("Introduceti un string: ")
caracter = input("Introduceti un caracter: ")
print(numar_caractere(caracter, string))

'''8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive.'''

def lista_pozitive(numere):
    numere_pozitive = []
    for numar in numere:
        if numar >= 0:
            numere_pozitive.append(numar)
    return numere_pozitive

lista_numere = [-45, 61, 29, -11, 18, 63]
print(f'Lista de numere pozitive este: {lista_pozitive(lista_numere)}')

'''9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.'''

def calcul_numere(x,y):
    if x>y:
        print(f"Primul număr {x} este mai mare decat al doilea nr {y}.")
    elif y>x:
        print(f"Al doilea nr {y} este mai mare decat primul nr {x}.")
    else:
        print(f"Numerele sunt egale.")

x=int(input("Introduceti un numar x: "))
y=int(input("Introduceti un numar y: "))
print(calcul_numere(x,y))

'''10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False'''

def functie (numar, set):
    if numar in set:
        print (f"nu am adaugat numărul în set. Acesta există deja")
        return "False"
    else:
        set.add(numar)
        print("am adaugat numărul nou în set")
        return "True"
set = {1,2,3,4,5,6,7,8,9,10}
numar=int(input("Introduceti un numar de la 1 la 20: "))
print(functie(numar,set))
print(set)
print(functie(numar,set))

'''Exerciții Opționale 
1. Funcție care primește o lună din an și returnează câte zile are acea luna'''

def zile_luna (luna):
    if luna in ["ianuarie", "martie", "mai", "iulie", "august", "octombrie", "decembrie"]:
        print(f"Luna {luna} are 31 de zile.")
    elif luna is ["februarie"]:
        print(f"Luna {luna} are 28 de zile.")
    else:
        print(f'Luna {luna} are 30 de zile.')

luna = input("Introduceti o luna a anului: ")
zile_luna(luna)

'''2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)'''

def calculator(x,y):
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return a,b,c,d

a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

'''3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}'''

lista = [ 3, 6, 7, 2, 1, 3, 5 , 2, 1, 9, 9, 9, 9, 5, 1, 9, 3, 4, 8, 6, 7, 5]
def count(lista):
    dictionar = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for i in dictionar.keys():
        for x in lista:
            if x == i:
                dictionar[i] = dictionar[i] + 1
    return dictionar

'''4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.'''

def returneaza_numar_maxim (x,y,z):
    if x> y and x>z:
        print(f"Numarul cel mai mare este: {x}.")
    elif y>x and y>z:
        print(f"Numarul cel mai mare este: {y}.")
    else:
        print(f"Numarul cel mai mare este: {z}.")

x, y, z = input("Introduceti 3 numere diferite:").split()
returneaza_numar_maxim(x,y,z)

'''5. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr. 
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)'''

def suma_num(numar):
    suma = 0
    for i in range(0, numar+1):
        suma=suma + i
    return suma
print(suma_num(5))

'''Exerciții Opționale - Bonus
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.
Exemplu: list1 = [1, 1, 2, 3], list2 = [2, 2, 3, 4]. Răspuns: {2, 3}'''

def numere_comune(list1, list2):
    return set(list1).intersection(list2)

list1 = [11, 3, 5, 4, 9]
print(f'Lista 1: {list1}')
list2 = [12, 11, 3, 7, 9]
print(f'Lista 2: {list2}')
print(f' Numere comune: {numere_comune(list1,list2)}.')

'''2. Funcție care să aplice o reducere de preț. Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.'''

def reducere_pret(pret):
    reducere = float(input("Introduceti reducerea procentuala: "))
    if reducere > 1 or reducere <0:
        print("Reducere invalida")
        input("Introduceti un procent de reducere valid: ")
    else:
        pret_dupa_reducere = pret*reducere
        print(f"Pretul dupa reducere este {pret_dupa_reducere}.")
reducere_pret(100)

'''3. Funcție care să afișeze data și ora curentă din Ro. (bonus: afișați și data și ora curentă din China)'''

'''4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun.'''
