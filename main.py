from Tests.testAll import testAll
from UI.commandLine import commandLine
from UI.console import meniu


def main():
    lista = []
    testAll()
    undoList = []
    redoList = []
    print("Toate functiile de calcul au trecut testele! Felicitari! ")
    while True:
        print("Pentru meniu tastati '1'. ")
        print("Pentru comenzi tastati '2'. ")
        print("Pentru a inchide tastati 'x'. ")
        print("Introduceti optiunea: ")
        optiune = input()
        if optiune == "1":
            meniu(lista, undoList, redoList)
        elif optiune == "2":
            lista = commandLine(lista, undoList, redoList)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati! ")


if __name__ == '__main__':
    main()
