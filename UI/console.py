from Domain.avion import toString
from Logic.CRUD import adaugaRezervare, stergereRezervare, modificaRezervare


def printMenu():
    print("1. Adauga rezervare. ")
    print("2. Sterge rezervare. ")
    print("3. Modifica rezervare. ")
    print("4. Trecerea tututror rezervarilor facute pe un nume citit la o clasa superioara. ")
    print("a. Afisare rezervare. ")
    print("x. Iesire. ")

def uiAdaugaRezervare(lista):
    id = input("Introduceti id-ul: ")
    nume = input("Introduceti numele: ")
    clasa = input("Introduceti clasa (economy/economy plus/business): ")
    pret = float(input("Introduceti pretul: "))
    checkin = str(input("Introduceti starea check-in-ului (DA/NU): "))
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)

def uiStergeRezervare(lista):
    id = input("Introduceti id-ul rezervarii de sters: ")
    return stergereRezervare(id, lista)

def uiModificaRezervare(lista):
    id = input("Introduceti id-ul rezervarii de modificat: ")
    nume = input("Introduceti noul nume: ")
    clasa = input("Introduceti noua clasa (economy/economy plus/business): ")
    pret = float(input("Introduceti noul pret: "))
    checkin = str(input("Introduceti noua stare a check-in-ului (DA/NU): "))
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)

def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))

def uiSchimbareClasa(lista):
    substringNume = input("Dati numele dupa care se va face modificarea: ")
    sClasa = str(input("Introduceti clasa actuala: "))
    return (substringNume, sClasa, lista)

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaRezervare(lista)
        elif optiune == "2":
            lista = uiStergeRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = uiSchimbareClasa(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
