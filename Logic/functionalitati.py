from Domain.avion import getNume, creeazaRezervare, getId, getClasa, getPret, getCheckin


def schimbareClasa(substringNume, sClasa, lista):
    """
    Trecerea tuturor rezervarilor facute pe un nume citit la o clasa superioara.
    :param substringNume: Numele persoanei pentru care se vor face schimbarile.
    :param sClasa: Clasa actuala.
    :param lista: Lista de rezervari.
    :return: Lista de rezervari reactualizata.
    """
    listaNoua = []
    for rezervare in lista:
        if substringNume in getNume(rezervare):
            if getClasa(rezervare) == "economy":
                id = getId(rezervare)
                nume = getNume(rezervare)
                clasa = creeazaRezervare(id, nume, "economy plus", pret, checkin)
                pret = getPret(rezervare)
                checkin = getCheckin(rezervare)
                listaNoua.append(clasa)
            elif getClasa(rezervare) == "economy plus":
                id = getId(rezervare)
                nume = getNume(rezervare)
                clasa = creeazaRezervare(id, nume, "business", pret, checkin)
                pret = getPret(rezervare)
                checkin = getCheckin(rezervare)
                listaNoua.append(clasa)
            else:
                listaNoua.append(rezervare)
    return listaNoua
