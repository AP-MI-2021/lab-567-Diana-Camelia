from copy import deepcopy
from Domain.rezervare import getNume, getClasa
from Domain.rezervare import getCheckin, getPret, creeazaRezervare, getAll


def afisareSumaPreturilorFiecareNume(lista):
    """
    Functia calculeaza suma preturilor pentru fiecare nume in parte.
    :param lista: lista
    :return: dictionar ce contine ca si cheie pentru fiecare nume, suma calculata.
    """

    suma = {}
    for rezervare in lista:
        numele = getNume(rezervare)
        pretul = getPret(rezervare)
        if numele in suma:
            suma[numele] = suma[numele] + pretul
        else:
            suma[numele] = pretul
    return suma


def determinarePretMaximClasa(lista):
    """
    Functia determina pretul maxim pentru fiecare clasa in parte.
    :param lista: lista
    :return: dictionar ce contine in cele 3 chei maximele gasite.
    """

    maximClasa = {}
    for rezervare in lista:
        cls = getClasa(rezervare)
        pretul = getPret(rezervare)
        if cls in maximClasa:
            if pretul > maximClasa[cls]:
                maximClasa[cls] = pretul
        else:
            maximClasa[cls] = pretul
    return maximClasa


def ieftiniri(procentaj, lista):
    """
    Functia aplica reduceri rezervarilor unde s-a facut checkin-ul
    :param procentaj: float
    :param lista: lista
    :return: lista cu reduceri aplicate(daca a fost cazul)
    """

    if procentaj > 100:
        raise ValueError("Nu se pot face reduceri mai mari de 100%! ")
    if procentaj < 0:
        raise ValueError("Procentajul nu trebuie sa fie mai mic decat 0! ")
    listaNoua = []
    for rezervare in lista:
        if getCheckin(rezervare) == "Da":
            noulPret = getPret(rezervare) - (procentaj / 100 * getPret(rezervare))
            id, nume, clasa, pret, checkin = getAll(rezervare)
            rezervareNoua = creeazaRezervare(id, nume, clasa, noulPret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def ordonare(lista):
    """
    Functia ordoneaza descrescator rezervarile
    :param lista: lista
    :return: rezervarile ordonate descrescator
    """

    listaNoua = deepcopy(lista)
    for i in range(0, len(listaNoua)-1):
        for j in range(i+1, len(listaNoua)):

            if getPret(listaNoua[i]) < getPret(listaNoua[j]):
                auxiliar = listaNoua[j]
                listaNoua[j] = listaNoua[i]
                listaNoua[i] = auxiliar

    return listaNoua
