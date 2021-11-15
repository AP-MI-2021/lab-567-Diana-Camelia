from Domain.rezervare import getNume, getClasa, toString, getAll, getId, creeazaRezervare


def adaugaRezervare(id, nume, clasa, pret, checkin, lista):
    """
    Functia adauga o noua rezervare in lista.
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista
    :return: lista cu detaliile noii rezervari din dictionar.
    """
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja! ")
    if clasa != "economy" and clasa != "economy plus" and clasa != "business":
        raise ValueError("Singurele clase sunt : economy/ economy plus/ business! ")
    if pret < 0:
        raise ValueError("Pretul trebuie sa fie un numar pozitiv! ")
    if checkin != "Da" and checkin != "Nu":
        raise ValueError("Checkinul se noteaza cu 'Da' sau 'Nu'! ")

    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def getById(id, lista):
    """
    Gaseste o rezervare dupa un id dat.
    :param id : id-ul rezevarii.
    :param lista : lista cu rezervari.
    :return: rezervarea cu id-ul primit, sau 'None', daca nu exista.
    """

    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare


def stergeRezervare(id, lista):
    """
    Functia sterge rezervarea cu id-ul dat.
    :param id: string
    :param lista: lista cu rezervari.
    :return: lista modificata ce contine toate rezervarile inafara de cea care s-a sters.
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista rezervare cu acest id! ")
    return [rezervare for rezervare in lista if getId(rezervare) != id]


def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    """
    Functia modifica valorile cheilor pentru un anume id dat.
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista
    :return: lista modificata.
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista rezervare cu acest id! ")
    if clasa != "economy" and clasa != "economy plus" and clasa != "business":
        raise ValueError("Singurele clase sunt : economy/ economy plus/ business")
    if pret < 0:
        raise ValueError("Pretul trebuie sa fie un numar pozitiv! ")
    if checkin != "Da" and checkin != "Nu":
        raise ValueError("Checkinul se noteaza cu 'Da' sau 'Nu'! ")
    lista_noua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervare_noua = creeazaRezervare(id, nume, clasa, pret, checkin)
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua


def modificareClasa(numeCitit, lista):
    """
    Functia trece toate rezervarile la o clasa superioara pentru un nume citit.
    :param nume_citit: string
    :param lista: lista
    :return: lista rezervarilor cu modificarea claselor (daca a fost cazul).
    """

    listaNoua = []
    for rezervare in lista:
        if getNume(rezervare) == numeCitit:
            if getClasa(rezervare) == "economy":
                nouaClasa = "economy plus"
            elif getClasa(rezervare) == "economy plus":
                nouaClasa = "business"
            else:
                print("Rezervarea " + toString(rezervare) + ", se afla deja la clasa superioara! ")
                nouaClasa = getClasa(rezervare)

            id, nume, clasa, pret, checkin = getAll(rezervare)
            rezervareClasaModificata = creeazaRezervare(id, nume, nouaClasa, pret, checkin)
            listaNoua.append(rezervareClasaModificata)
        else:
            listaNoua.append(rezervare)

    return listaNoua
