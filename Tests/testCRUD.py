from Domain.rezervare import getId, getNume, getPret, getCheckin, getClasa
from Logic.CRUD import adaugaRezervare, getById, stergeRezervare, modificaRezervare, modificareClasa


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Diana", "economy plus", 200, "Nu", lista)
    assert getId(lista[0]) == "1"
    assert getNume(lista[0]) == "Diana"
    assert getById("1", lista) == lista[0]
    assert getId(getById("1", lista)) == "1"
    lista = adaugaRezervare("2", "Camelia", "economy plus", 200, "Da", lista)
    assert getId(lista[1]) == "2"
    assert len(lista) == 2


def testStergeRezervare():
    lista = []
    lista = adaugaRezervare("1", "Diana", "economy plus", 200, "Nu", lista)
    lista = adaugaRezervare("2", "Camelia", "economy plus", 200, "Da", lista)
    lista = stergeRezervare("1", lista)
    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getId(lista[0]) == "2"


def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adaugaRezervare("2", "Adrian", "economy plus", 200, "Da", lista)
    lista = modificaRezervare("1", "Mihai", "economy", 210, "Da", lista)
    assert getNume(getById("1", lista)) == "Mihai"
    assert getPret(getById("1", lista)) == 210
    assert getCheckin(getById("1", lista)) == "Da"


def testModificareClasa():
    lista = []
    lista = adaugaRezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adaugaRezervare("2", "Adrian", "economy plus", 100, "Da", lista)
    lista = modificareClasa("Adi", lista)
    assert getClasa(lista[0]) == "business"
    assert getClasa(lista[1]) == "economy plus"
    lista = modificareClasa("Adrian", lista)
    assert getClasa(lista[1]) == "business"
