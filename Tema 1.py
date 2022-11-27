''' 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
O variabila este o adresa de memorie la care putem sa stocam anumite valori, iar mai apoi daca e nevoie, sa le schimbam.'''

''' 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă: string, int, floar, bool: '''
materie = "algebra"
inaltime = 90
diagonala = 36.33
test_promovat = True

'''3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.'''
print(type(materie))
print(type(inaltime))
print(type(diagonala))
print(type(test_promovat))

'''Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere). Verifică tipul acesteia.'''
diagonala=round(diagonala)
print(type(diagonala))

'''5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.'''
print(f'Materia lui preferata este {materie}.')
print(f'Copilul are {inaltime} de cm inaltime.')
print(f'Rezultatul calculului diagonalei este {diagonala} m.')
print(f'Test promovat de catre toti studentii: {test_promovat}.')

'''6. Citește de la tastatură: numele; prenumele. Afișează: 'Numele complet are x caractere'.'''
nume=input("Introduceti numele:")
prenume=input("Introduceti prenumele:")
nume_complet=nume+prenume
print(f'Numele complet are {len(nume_complet)} caractere.')

'''7. Citește de la tastatură: lungimea; lățimea. Afișează: 'Aria dreptunghiului este x'.'''
lungimea = int(input("Introdu lungimea:"))
latimea = int(input("Introdu latimea:"))
aria_dreptunghiului = lungimea*latimea
print(f'Aria dreptunghiului este {aria_dreptunghiului}.')

'''8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the'.'''

sir = 'Coral is either the stupidest animal or the smartest rock'
numara = sir.count('the')
print(f'Cuvantul "the" apare de {numara} ori.')

'''9. Același string. Afișează de câte ori apare cuvântul 'the'. Printează rezultatul.'''

sir = 'Coral is either the stupidest animal or the smartest rock'
numara = sir.count(' the ')
print(f'Cuvantul "the" apare ca si cuvant separat de {numara} ori.')

'''10. Același string. Folosiți un assert ca să verificați dacă acest string conține doar numere.'''
sir = 'Coral is either the stupidest animal or the smartest rock'
print(sir.isdecimal())

'''Exerciții Opționale 
1. Citește de la tastatură un string de dimensiune impară. Afișează caracterul din mijloc.'''

sir_impar=input("Introd 5 caractere:")
caracter_mijloc=sir_impar[len(sir_impar)//2]
print(f'Caracterul din mijloc al sirului introdus este: {caracter_mijloc}.')

'''2. Folosind assert, verifică dacă un string este palindrom.'''

cuvant=input("Introdu cuvantul pentru a verifica daca e palindrom:")
cuvant_reverse=cuvant[::-1]
assert cuvant == cuvant_reverse, 'Eroare: nu este palindrom'

'''3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.'''

cuvinte=input("Introdu oricare 2 cuvinte:")
primul_cuvant = cuvinte.split( )[0]
al_doilea_cuvant = cuvinte.split( ) [-1]
print(primul_cuvant)
print(al_doilea_cuvant)

'''4. Citește un string de la tastatură (ex: alabala portocala).
Salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
Capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul. caracter => alAbAlA portocAla.'''

text=input("Introdu un string:")
primul_caracter = text[0] #am identificat prima litera
ultimul_caracter = text [-1]
text_modificat=text.upper()
print(primul_caracter+text_modificat[1:-1]+ultimul_caracter)

'''5. Citește un user de la tastatură. Citește o parolă. Afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
eg: parola abc => ***
parola abcd => ****'''

user = input("Introdu user:")
parola = input("Introdu parola:")
nr_caractere_parola = len(parola)
parola_ascunsa='*'* nr_caractere_parola
print(f'Parola pentru userul {user} este {parola_ascunsa} si are {nr_caractere_parola} caractere.')