from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificareClasa, modificaRezervare
from Logic.functionalitati import ieftiniri, ordonare, afisareSumaPreturilorFiecareNume, determinarePretMaximClasa


def menu(undoList, redoList):
    print("1. Adauga rezervare. ")
    print("2. Sterge rezervare. ")
    print("3. Modifica rezervare. ")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară. ")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit. ")
    print("6. Determinarea prețului maxim pentru fiecare clasă. ")
    print("7. Afisarea rezervărilor ordonate descrescător după preț. ")
    print("8. Afișarea sumelor prețurilor pentru fiecare nume. ")
    if len(undoList) > 0:
        print("u. Undo. ")
    if len(redoList) > 0:
        print("r. Redo. ")
    print("a. Afiseaza rezervari. ")
    print("x. Iesire. ")


def uiAdaugare(lista, undoList, redoList):
    """
    Functia citeste datele noii rezervari.
    :param redo_list: lista in care exista datele inaintea folosirii undo(daca s-a folosit).
    :param undo_list: lista in care se retin rezervarile inainte de adaugare.
    :param lista: lista
    :return: lista in urma adaugarii.
    """
    try:
        id = input("Introduceti id-ul rezervarii: ")
        nume = input("Introduceti numele: ")
        clasa = input("Introduceti clasa (economy/ economy plus/ business): ")
        pret = float(input("Introduceti pretul: "))
        checkin = input("Introduceti starea check-in-ului (Da/Nu): ")
        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergere(lista, undoList, redoList):
    """
    Functia sterge o rezervarea cu id -ul dat.
    :param redo_list: lista in care exista datele inaintea folosirii undo(daca s-a folosit).
    :param undo_list: lista in care se retin rezervarile inainte de stergere.
    :param lista: lista
    :return: lista in urma stergerii.
    """
    try:
        id = input("Introduceti id-ul rezervarii pe care doriti sa o stergeti: ")
        rezultat = stergeRezervare(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificare(lista, undo_list, redo_list):
    """
    Functia citeste id-ul rezervarii unde vor exista modificari + elementele modificate (unde se doreste modificarea).
    :param redo_list: lista in care exista datele inaintea folosirii undo(daca s-a folosit).
    :param undo_list: lista in care se retin rezervarile inainte de modificare.
    :param lista: lista.
    :return: lista in urma modificarii unei rezervari.
    """
    try:
        id = input("Introduceti id-ul rezervarii pe care doriti sa o modificati: ")
        nume = input("Introduceti noul nume: ")
        clasa = input("Introduceti noua clasa: ")
        pret = float(input("Introduceti noul pret: "))
        checkin = input("Introduceti  noua stare a check-in-ului (Da/Nu): ")
        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    """
    Functia afiseaza toate rezervarile (lista).
    :param lista: lista
    :return: rezervarile.
    """
    if len(lista) > 0:
        for rezervare in lista:
            print(toString(rezervare))
    else:
        print("Nu exista rezervari! ")


def uiIeftinire(lista, undoList, redoList):
    """
    Functia citeste procentajul cu care se vor reduce rezervarile la care s-a facut checkin-ul.
    :param redo_list: lista in care exista datele inaintea folosirii undo(daca s-a folosit).
    :param undo_list: lista in care se retin rezervarile inainte de ieftinire.
    :param lista: lista
    :return: rezervarile in urma ieftinirilor.
    """
    try:
        procentaj = float(input("Introduceti procentajul cu care doriti sa se reduca pretul rezervarilor cu check-in-ul: "))
        rezultat = ieftiniri(procentaj, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificareClasa(lista, undoList, redoList):
    """
    Functia citeste numele persoanei careia i se va modifica clasa intr-una superiora
    :param redo_list: lista in care exista datele inaintea folosirii undo(daca s-a folosit)
    :param undo_list: lista in care se retin rezervarile inainte de modificare clasa
    :param lista: lista
    :return: rezervarile in urma trecerii la o clasa superioara ( pentru un anume nume citit)
    """

    numeCitit = input("Introduceti numele persoanei careia trebuie modificata superior clasa: "
                       " (un singur nume) ")
    rezultat = modificareClasa(numeCitit, lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat



def uiDeterminarePretMaximClasa(lista):
    """
    Functia afiseaza pentru fiecare clasa pretul maxim.
    :param lista: lista
    :return: None (doar afiseaza)
    """
    maximClasa = determinarePretMaximClasa(lista)
    for clasa in maximClasa:
        print("Clasa {} are pretul cel mai mare, in valoare de : {}".format(clasa,
                                                                maximClasa[clasa]))
    return None


def uiOrdonare(lista):
    """
    Functia afiseaza rezervarile ordonate descrescator.
    :param lista: lista.
    :return: None (doar afiseaza).
    """

    lista_ordonata = ordonare(lista)
    if len(lista_ordonata) > 0:
        print("Rezervarile ordonate descrescator sunt : ")
        showAll(lista_ordonata)
    else:
        print("Nu exista rezervari! ")


def uiAfisareSumaPreturilorFiecareNume(lista):
    """
    Functia afiseaza pentru fiecare nume, suma preturilor.
    :param lista: lista
    :return: None (doar afiseaza).
    """

    suma = afisareSumaPreturilorFiecareNume(lista)
    for nume in suma:
        print("{} are suma de: {} ". format(nume, suma[nume]), "lei.")


def meniu(lista, undoList, redoList):
    while True:
        menu(undoList, redoList)
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            lista = uiAdaugare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergere(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiModificareClasa(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiIeftinire(lista, undoList, redoList)
        elif optiune == "6":
            uiDeterminarePretMaximClasa(lista)
        elif optiune == "7":
            uiOrdonare(lista)
        elif optiune == "8":
            uiAfisareSumaPreturilorFiecareNume(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo! ")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo! ")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            print("La revedere! ")
            break
        else:
            print("Optiune gresita! Reincercati! ")
