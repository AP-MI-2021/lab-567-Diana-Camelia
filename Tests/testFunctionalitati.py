from Domain.rezervare import getPret, getId
from Logic.CRUD import adaugaRezervare
from Logic.functionalitati import determinarePretMaximClasa, ieftiniri, ordonare, afisareSumaPreturilorFiecareNume


def testAfisareSumaPreturilorFiecareNume():
    lista = []
    lista = adaugaRezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adaugaRezervare("2", "Marcel", "economy plus", 100, "Da", lista)
    lista = adaugaRezervare("3", "Marcel", "economy", 500, "Da", lista)
    lista = adaugaRezervare("4", "Ricardo", "economy", 500, "Da", lista)
    suma = afisareSumaPreturilorFiecareNume(lista)
    assert suma["Marcel"] == 600
    assert suma["Adi"] == 200
    assert suma["Ricardo"] == 500


def testDeterminarePretMaximClasa():
    lista = []
    lista = adaugaRezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adaugaRezervare("2", "Adrian", "economy plus", 100, "Da", lista)
    lista = adaugaRezervare("3", "Marcel", "economy", 500, "Da", lista)
    lista = adaugaRezervare("4", "Dorel", "business", 2000, "Da", lista)
    maxim_cls = determinarePretMaximClasa(lista)
    assert maxim_cls["economy"] == 500
    assert maxim_cls["economy plus"] == 200
    assert maxim_cls["business"] == 2000


def testIeftiniri():
    lista = []
    lista = adaugaRezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adaugaRezervare("2", "Adrian", "economy plus", 100, "Da", lista)
    lista = ieftiniri(10, lista)
    assert getPret(lista[1]) == 90.0
    lista = ieftiniri(10, lista)
    assert getPret(lista[1]) == 81.0
    assert getPret(lista[0]) == 200


def testOrdonare():
    lista = []
    lista = adaugaRezervare("1", "Adi", "economy plus", 200, "Nu", lista)
    lista = adaugaRezervare("2", "Adrian", "economy plus", 100, "Da", lista)
    lista = adaugaRezervare("3", "Marcel", "business", 210, "Nu", lista)
    listaNoua = ordonare(lista)
    assert getId(listaNoua[0]) == "3"
    assert getId(listaNoua[1]) == "1"
    assert getId(listaNoua[2]) == "2"
    assert getId(lista[0]) == "1"
