from Domain.avion import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaRezervare, getById, stergereRezervare, modificaRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare(1, "mihai", "business", 149.99, "DA", lista)

    assert len(lista) == 1
    assert getId(lista[0]) == 1
    assert getNume(lista[0]) == "mihai"
    assert getClasa(lista[0]) == "business"
    assert getPret(lista[0]) == 149.99
    assert getCheckin(lista[0]) == "DA"

def testGetById():
    lista = []
    lista = adaugaRezervare(1, "mihai", "business", 149.99, "DA", lista)
    lista = adaugaRezervare(2, "diana", "economy", 29.99, "NU", lista)
    lista = adaugaRezervare(3, "marcela", "economy plus", 75.99, "DA", lista)

    assert len(lista) == 3
    assert getId(getById("1", lista)) == 1
    assert getNume(getById("1", lista)) == "mihai"
    assert getClasa(getById("1", lista)) == "business"
    assert getPret(getById("1", lista)) == 149.99
    assert getCheckin(getById("1", lista)) == "DA"

def testStergerePrajitura():
    lista = []
    lista = adaugaRezervare(1, "mihai", "business", 149.99, "DA", lista)
    lista = adaugaRezervare(2, "diana", "economy", 29.99, "NU", lista)
    lista = adaugaRezervare(3, "marcela", "economy plus", 75.99, "DA", lista)

    lista = stergereRezervare("1", lista)
    assert len(lista) == 2
    assert getById("1", lista) is None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None

    lista = stergereRezervare("3", lista)
    assert len(lista) == 1
    assert getById("2", lista) is not None

def testModificaRezervare():
    lista = []
    lista = adaugaRezervare(1, "mihai", "business", 149.99, "DA", lista)
    lista = adaugaRezervare(2, "diana", "economy", 29.99, "NU", lista)
    lista = adaugaRezervare(3, "marcela", "economy plus", 75.99, "DA", lista)
    lista = modificaRezervare(3, "ana", "economy", 34.99, "DA", lista)

    rezervareUpdatata = getById("2", lista)
    assert getId(rezervareUpdatata) == 2
    assert getNume(rezervareUpdatata) == "diana"
    assert getClasa(rezervareUpdatata) == "economy"
    assert getPret(rezervareUpdatata) == 29.99
    assert getCheckin(rezervareUpdatata) == "NU"

