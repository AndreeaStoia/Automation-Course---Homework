'''Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe. X este un int.
1. Declară o listă note_muzicale în care să pui do re mi etc până la do.
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.'''

note_muzicale = ['do', 're', 'mi', 'fa', 'so', 'la', 'si', 'do']
print(note_muzicale)
print(note_muzicale[::-1])
note_muzicale.reverse()
print(note_muzicale)

'''2. De câte ori apare ‘do’?'''

note_muzicale = ['do', 're', 'mi', 'fa', 'so', 'la', 'si', 'do']
print(note_muzicale.count('do'))

'''3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]. Găsește 2 variante să le unești într-o singură listă.'''

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1 + lista2
print(lista3)

lista1.extend(lista2)
print(lista1)

'''4.
● Sortează și afișază lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.'''

lista1.sort()
print(lista1)
lista1.remove(0)
print(lista1)

'''5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.'''

if lista1 == []:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')

'''6. Folosește o funcție care să șteargă lista de la exercițiul 3.'''

lista1.clear()
print(lista1)

'''7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.'''

if lista1 == []:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')

'''8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)'''

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

'''9. Printează cei 3 elevi și notele lor. Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie'''

print(f'Ana a luat nota {dict1["Ana"]}.')
print(f'Gigel a luat nota {dict1["Gigel"]}.')
print(f'Dorel a luat nota {dict1["Dorel"]}.')

'''10. Dorel a făcut contestație și a primit 6. Modifică nota lui Dorel în 6. Printează nota după modificare'''

dict1.update({'Dorel': 6})
print(f'Dorel a luat nota {dict1["Dorel"]}.')

'''11. Gigel se transferă din clasă.
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi.'''

dict1.pop('Dorel')
print(dict1)

dict1['Ionica']=9
print(dict1)

'''12. Set zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}. Adaugă în zilele_sapt ‘luni’. Afișeaza zile_sapt'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni') #nu exista duplicate
print(zile_sapt)

'''13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.'''

if weekend.issubset(zile_sapt):
    print(f'Weekend este un subset al zilelor saptamanii')
else:
    print(f'Weekend nu este un subset al zilelor saptamanii')

'''14. Afișează diferențele dintre aceste 2 seturi.'''

print(zile_sapt.difference(weekend))

'''15. Afișază intersecția elementelor din aceste 2 seturi.'''
print(zile_sapt.intersection(weekend))

'''Exercitii optionale. 
1. Ne imaginăm o echipă de fotbal pt teren sintetic.3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3'''

jucatori = ['Marian', 'Ionut', 'Codrin','Andrei', 'Tudor']

SCHIMBARI_MAXIME = 3
schimbari_efectuate = 0
# calculam si initializam schimbari ramase
schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
lista_jucatori_teren = ['j1', 'j2', 'j3', 'j4', 'j5']
lista_jucatori_rezerva = ['j6','j7','j8','j9','j10']
lista_jucatori_scosi = []
jucator_in = 'j6'
jucator_out = 'j1'
# daca jucatorul e in teren SI daca mai am schimbari
if jucator_out in lista_jucatori_teren and schimbari_ramase > 0:
   if jucator_in in lista_jucatori_rezerva and jucator_in not in lista_jucatori_teren: # eliminam cazul cand jucatorul este deja in teren
       lista_jucatori_teren.remove(jucator_out)  # scoatem jucatorul
       lista_jucatori_scosi.append(jucator_out)
       lista_jucatori_teren.add(jucator_in)  # adaugam jucatorul nou
       lista_jucatori_rezerva.remove(jucator_out)
       schimbari_ramase = schimbari_ramase - 1  # contorizam schimbarea
       print(f'Schimbare efectuata cu succes!')
       print(f'A intrat {jucator_in}, a iesit {jucator_out}, mai aveti {schimbari_ramase} schimbari')
else:
   if schimbari_ramase <= 0:
       print('Nu mai ai schimbari')
   else:
       print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren')
print(f'Actuala echipa este {echipa}')
print(f"Jucatorii care au fost scosi sunt: {lista_jucatori_scosi}")

