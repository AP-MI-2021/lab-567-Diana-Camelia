from Logic.CRUD import adaugaRezervare
from Tests.TestAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare(1, "mihai", "business", 149.99, "DA", lista)
    lista = adaugaRezervare(2, "diana", "economy", 29.99, "NU", lista)
    lista = adaugaRezervare(3, "marcela", "economy plus", 75.99, "DA", lista)
    lista = adaugaRezervare(4, "gabi", "business", 199.99, "DA", lista)
    runMenu(lista)


main()