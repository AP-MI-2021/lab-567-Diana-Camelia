from Domain.avion import creeazaRezervare, getId


def adaugaRezervare(id, nume, clasa, pret, checkin, lista):
    """
    Adauga o rezervare intr-o lista.
    :param id: Id-ul rezervarii.
    :param nume: Numele rezervarii.
    :param clasa: Clasa rezervarii.
    :param pret: Pretul rezervarii.
    :param checkin: Check-in-ul rezervarii.
    :param lista: O lista continand, atat vechile rezervari, cat si rezervarea nou adaugata.
    :return:
    """
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]

def getById(id,lista):
    '''
    Da elementul din lista cu un id dat.
    :param id: Id-ul prajiturii de cautat.
    :param lista: Lista de prajituri.
    :return: Prajitura cu id-ul dat, sau, in caz contrar, None, dac nu exista.
    '''
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None

def stergereRezervare(id, lista):
    '''
    Sterge rezervarea cu id-ul dat dintr-o lista.
    :param id: Id-ul rezervarii de sters.
    :param lista: Lista de rezervari.
    :return: Lista ce contine toate celelalte rezervari in afara de cea stearsa.
    '''
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    """
    Modifica datele unei rezervari (inafara de id, care nu se va schimba niciodata).
     :param id: Id-ul rezervarii.
    :param nume: Numele rezervarii.
    :param clasa: Clasa rezervarii.
    :param pret: Pretul rezervarii.
    :param checkin: Check-in-ul rezervarii.
    :param lista: Lista de rezervari.
    :return: Lista cu rezervarea modificata.
    """
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

