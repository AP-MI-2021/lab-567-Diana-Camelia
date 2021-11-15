from copy import deepcopy

from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from UI.console import showAll


def commandLine(lista, undo_list, redo_list):
    while True:
        try:
            print("Pentru ajutor tastati 'HELP'! ")
            comanda = input("Introduceti comanda: ")
            if comanda == "HELP":
                print(" Pentru a adauga o noua rezervare scrieti comanda 'add' urmata de datele")
                print("pe care doriti sa le introduceti, separate prin virgula! ")
                print(" Pentru a modifica, scrieti 'update',apoi virgula si id-ul rezervarii ce urmeaza ")
                print("sa fie modificata, urmat de noile date! ")
                print(" Pentru a sterge, scrieti 'delete', apoi virgula si id-ul rezerarii ce urmeaza sa se stearga! ")
                print(" Pentru a face undo, tastati 'undo'! ")
                print(" Pentru a face redo, tastati 'redo'! ")
                print(" Pentru a afisa toate datele, scrieti 'showall'! ")
                print(" Pentru a iesi scrieti 'stop'. ")
                print(" Puteti scrie mai multe comenzi separandu-le prin ';'. ")
                print(" Exemple: ")
                print(" add,1,Ana,business,149.99,Da")
                print(" add,2,Albert,economy,250.50,Nu")
                print(" undo;redo")
                print(" showall;")
                print(" delete,2;showall")
                print(" update,1,Dorel,economy plus,100,Nu")
            else:
                executaComenzi = comanda.split(";")
                for i in range(len(executaComenzi)):
                    comandaSeparata = executaComenzi[i].split(",")
                    if comandaSeparata[0] == "add":
                        if len(comandaSeparata) != 6:
                            raise ValueError("Trebuie sa introduceti exact 5 date! ")
                        id = comandaSeparata[1]
                        nume = comandaSeparata[2]
                        clasa = comandaSeparata[3]
                        pret = float(comandaSeparata[4])
                        checkin = comandaSeparata[5]
                        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
                        undo_list.append(lista)
                        redo_list.clear()
                        lista = deepcopy(rezultat)
                    elif comandaSeparata[0] == "delete":
                        id = comandaSeparata[1]
                        rezultat = stergeRezervare(id, lista)
                        undo_list.append(lista)
                        redo_list.clear()
                        lista = deepcopy(rezultat)
                        print("Au fost sterse date! ")
                    elif comandaSeparata[0] == "update":
                        if len(comandaSeparata) != 6:
                            raise ValueError("Trebuie sa introduceti exact 5 date! ")
                        id = comandaSeparata[1]
                        nume = comandaSeparata[2]
                        clasa = comandaSeparata[3]
                        pret = float(comandaSeparata[4])
                        checkin = comandaSeparata[5]
                        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista)
                        undo_list.append(lista)
                        redo_list.clear()
                        lista = deepcopy(rezultat)
                        print("Au fost modificate date! ")
                    elif comandaSeparata[0] == "showall":
                        showAll(lista)
                        print("S-a afisat un set de date! ")
                    elif comandaSeparata[0] == "undo":
                        if len(undo_list) > 0:
                            redo_list.append(lista)
                            lista = undo_list.pop()
                        else:
                            print("Nu se poate face undo! ")
                    elif comandaSeparata[0] == "redo":
                        if len(redo_list) > 0:
                            undo_list.append(lista)
                            lista = redo_list.pop()
                        else:
                            print("Nu se poate face redo! ")
                    elif comandaSeparata[0] == "stop":
                        return lista
                    else:
                        print("Comanda gresita! Reincercati! ")
        except ValueError as ve:
            print("Eroare: {}".format(ve))
