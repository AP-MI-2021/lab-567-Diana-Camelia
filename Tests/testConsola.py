from Domain.rezervare import getId
from Logic.CRUD import adaugaRezervare, modificareClasa
from Logic.functionalitati import ieftiniri


def testUndoRedo():
    # Simularea scenariului primit de teste.
    # Nu este necesar sa testam si (undo, redo) in command_line!

    # lista , undoLista, redoLista sunt goale la inceput.
    lista = []
    undoList = []
    redoList = []

    # In cazul primelor simulari de adaugare, nu e necesar sa scriem redoList.append(lista).
    # deoarece ca nu s-a facut undo, redo fiind indisponibil.

    # Se adauga prima rezervare:
    rezultat = adaugaRezervare("1", "Marcel", "business", 200, "Da", lista)
    undoList.append(lista)
    lista = rezultat

    # Se adauga a 2-a rezervare:
    rezultat = adaugaRezervare("2", "Marcel2", "business", 2000, "Da", lista)
    undoList.append(lista)
    lista = rezultat

    # se adauga a 3-a rezervare:
    rezultat = adaugaRezervare("3", "Marcel3", "business", 20, "Da", lista)
    undoList.append(lista)
    lista = rezultat

    # Testarea pentru cele 3 obiecte adaugate:
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "3"


    # Realizam undo + assert:
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert undoList == [[], [['1', 'Marcel', 'business', 200, 'Da']]]

    # Se realizeaza inca un undo + assert:
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    # Se realizeaza inca un undo + assert:
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert undoList == []
    assert getId(redoList[2][0]) == "1"

    # Realizam inca un undo + assert (fara efect)
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList
    assert len(lista) == 0
    assert undoList == []
    assert getId(redoList[2][0]) == "1"

    # Adaugam 3 rezervari + assert (testare):
    rezultat = adaugaRezervare("1", "Marcel", "business", 200, "Da", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    rezultat = adaugaRezervare("2", "Marcel3", "business", 2000, "Da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("3", "Marcel3", "business", 20, "Da", lista)
    undoList.append(lista)
    lista = rezultat

    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    # Realizam redo (fara efect):
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    # Realizam 2 undo-uri + assert-uri (teste):
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert undoList == [[], [['1', 'Marcel', 'business', 200, 'Da']]]

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    # Realizam redo + assert (test):
    undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert len(lista) == 2

    # Realizam redo + assert (test):
    undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    # Realizam 2 undo-uri + assert-uri (teste):
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert undoList == [[], [['1', 'Marcel', 'business', 200, 'Da']]]

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]


    # Adaugam rezervarea cu id-ul 4:
    rezultat = adaugaRezervare("4", "Marcel4", "economy", 200, "Da", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    # Realizam redo (fara efect):
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(undoList) == 2
    assert undoList == [[], [['1', 'Marcel', 'business', 200, 'Da']]]

    # Facem undo:
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert len(undoList) == 1
    assert len(redoList) == 1

    # Realizam undo:
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert len(undoList) == 0
    assert len(redoList) == 2

    # Realizam doua redo-uri:
    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 1

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0

    # Realizam ultimul redo:
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0
    assert len(undoList) == 2

    # Teste cu assert și pentru operațiunile care modifică mai multe entități.
    # test modificare clasa superioara:
    nume = "Marcel4"
    undoList.append(lista)
    redoList.clear()

    lista = modificareClasa(nume, lista)
    assert lista[1][2] == "economy plus"

    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 2
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert lista[1][2] == "economy"

    undoList.append(lista)
    lista = redoList.pop()
    assert lista[1][2] == "economy plus"

    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 2
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert lista[1][2] == "economy"

    # test ieftinire + undo + assert-uri (teste):
    procentaj = 100
    undoList.append(lista)
    redoList.clear()

    lista = ieftiniri(procentaj, lista)
    assert lista[1][3] == 0

    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 2
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert lista[1][3] == 200

    undoList.append(lista)
    lista = redoList.pop()
    assert lista[1][3] == 0

    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 2
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert lista[1][3] == 200
