'''1.Având lista: mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# FOR
for i in range (len(masini)):
    print(f'Masina mea preferata este {masini[i]}.')

# FOR EACH
for masina in masini:
    print(f"Masina mea preferata este {masina}.")

# WHILE
i=0
while i< len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i+=1

'''2. Aceeași listă. Folosește un for else
În for: Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else: Printează lista.'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for i in range (1,len(masini)-1):
    masini[i]=masini[i].upper()
else:
    print(masini)

'''3. Aceeași listă. Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes: Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel: Printează ‘Am găsit mașina X. Mai căutam‘'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print('Am găsit mașina dorită de dvs.')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam.')

'''4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun: Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
- Printează S-ar putea să vă placă mașina x.'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == "Trabant" or masina == "Lăstun":
        continue
    print(f"S-ar putea sa va placa {masina}.")

'''5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina =='Lăstun' or masina=='Trabant':
        masini_vechi.append(masina)
print(masini_vechi)

i = 0
while i < len(masini):
    if masini[i] == 'Trabant' or masini[i] == 'Lăstun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
    i += 1
print(f'Masini vechi: {masini_vechi}.')
print(f'Masini noi: {masini}.')

'''6. Având dict:
pret_masini = {'Dacia': 6800,
               'Lăstun': 500,
               'Opel': 1100,
               'Audi': 19000,
               'BMW': 23000}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează: Pentru un buget de sub 15000 euro puteți alege mașină xLastun
● Iterează prin listă.'''

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}