'''1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

If else = o modalitate prin dam instructiuni ce se vor executa in functie de rezultatul evaluarii unor conditii.
Vom specifica ce se intampla daca conditiile sunt respectate si putem specifica si ce se va intampla daca nu sunt.
'''

'''2. Verifică și afișează dacă x este număr natural sau nu.'''

x=int(input("Introdu un numar:"))
if x > 0:
    print(f"Numarul {x} este un numar natural.")
else:
    print(f"Numarul {x} nu este un numar natural.")

'''3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.'''

x=int(input("Introdu un numar:"))
if x==0:
    print(f'Numarul {x} este un numar neutru.')
elif x>0:
    print(f'Numarul {x} este un numar pozitiv')
else:
    print(f'Numarul {x} este un numar negativ.')

'''4. Verifică și afișează dacă x este între -2 și 13.'''

x=int(input("Introdu un numar:"))
if x>-2 and x<13:
    print(f"Numarul {x} este cuprins intre 2 si 13.")
else:
    print(f'Numarul {x} nu este cuprins intre -2 si 13.')

'''5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.'''
x=int(input("Introdu un numar:"))
y=int(input("Introdu un alt numar:"))
if (x-y)<5:
    print(f"Diferenta dintre {x} si {y} este mai mica de 5.")
else:
    print(f'Diferenta dintre {x} si {y} nu este mai mica decat 5.')

'''6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.'''

x=int(input("Introdu un numar:"))
if not (x>5 and x<27):
    print(f"{x} nu este cuprins intre 5 si 27.")
else:
    print(f"{x} este cuprins intre 5 si 27.")

'''7. x și y (int). Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.'''
x=int(input("Introdu un numar:"))
y=int(input("Introdu un alt numar:"))
if x == y:
    print(f"{x} si {y} sunt egale.")
elif x>y:
    print(f"{x} este mai mare decat {y}.")
else:
    print(f"{y} este mai mare decat {x}.")

'''8. X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.'''
x=int(input('Introduceti un numar x:'))
y=int(input("Introdu un alt numar:"))
z=int(input("Introdu un alt numar:"))
if x==y==z:
    print("Triunghiul este echilateral")
elif x==y:
    print("Triunghiul este isoscel")
else:
    print("Triunghiul este oarecare")

'''9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu'''

x = input('Introdu o litera la alegere:')
if x.upper()=='A' or x.upper()=='E' or x.upper()=='I' or x.upper()=='O' or x.upper()=='U':
   print('Litera introdusa este o vocala')
else:
   print('Litera introdusa este o consoana')

'''10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F'''

nota = int(input('Introdu o nota de la 1 la 10:'))
if nota >=9:
    print("Echivalentul notei este A.")
elif nota >=8:
    print("Echivalentul notei este B.")
elif nota >=7:
    print('Echivalentul notei este C.')
elif nota >=6:
    print('Echivalentul notei este D.')
elif nota >=5:
    print('Echivalentul notei este E.')
else:
    print('Echivalentul notei este F.')

'''Exerciții Opționale.
1.Verifică dacă x are minim 4 cifre (x e int). (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)'''

x=int(input('Introdu un numar:'))
if x>=1000:
    print('Numarul x are minim 4 cifre')
else:
    print('Numarul x nu are minim 4 cifre')

'''2.Verifică dacă x are exact 6 cifre.'''
x=int(input('Introdu un numar:'))
y=len(str(x))
if y==6:
   print(f"Numarul {x} are exact 6 cifre.")
else:
    print(f"Numarul {x} nu are 6 cifre.")

'''3.Verifică dacă x este număr par sau impar (x e int).'''
x=int(input('Introdu un numar:'))
if x%2==0:
    print(f"Numarul {x} este par.")
else:
    print(f"Numarul {x} este impar.")

'''4. x, y, z (int). Afișează care este cel mai mare dintre ele?'''
x=int(input('Introduceti un numar x:'))
y=int(input("Introdu un alt numar:"))
z=int(input("Introdu un alt numar:"))
if x>y and x>z:
    print(f'Cel mai mare numar este {x}')
elif y>x and y>z:
    print(f'Cel mai mare numar este {y}')
else:
    print(f'Cel mai mare numar este {z}')

'''5. X, y, z reprezintă unghiurile unui triunghi. Verifică și afișează dacă triunghiul este valid sau nu.'''

x=int(input('Introduceti lungimea laturii x:'))
y=int(input('Introduceti lungimea laturii y:'))
z=int(input('Introduceti lungimea laturii z:'))
if x+y>z and x+z>y and y+Z>x:
    print('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')

'''6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citiți de la tastatură un int x
● Afișează stringul fără ultimele x caractere. Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'''

sir='Coral is either the stupidest animal or the smartest rock'
x=int(input("Introdu un numar de la 1 la 57:"))
print(sir[0:-x])

'''7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5'''
sir ='Coral is either the stupidest animal or the smartest rock'
sir2 = sir[0:5]+sir[-5:]

sir ='Coral is either the stupidest animal or the smartest rock'
sir2 = sir[0:5]+sir[-5:]
print(sir2)

'''8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvant
● output: 'Coral is either the stupidest animal or the smartest '''

sir ='Coral is either the stupidest animal or the smartest rock'
variabila=int(sir.index('rock'))
print(sir[:variabila])

'''9. Citește de la tastatura un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat'''

sir=input("Introdu un string:")
assert sir[0].upper()== sir[-1].upper(), "Cele 2 caractere nu sunt la fel"

'''10. Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)'''

sir='0123456789'
numere_pare = print(sir[0::2])
numere_impare = print(sir[1::2])

'''Exercitiu bonus. 
11. Joc ghicit zarul.
Caută pe net și vezi cum se generează un număr random. Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Luați un numărul ghicit de la utilizator. Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni:
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y. Joc ghicit zarul'''

x=int(input('Introdu un numar de la 1 la 6:'))
import random
y=random.randint(1,6)
if x<y:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {y}')
elif x>y:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {y}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {x} si zarul a fost {y}')

