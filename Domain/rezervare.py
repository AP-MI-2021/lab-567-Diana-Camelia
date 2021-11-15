def creeazaRezervare(id, nume, clasa, pret, checkin):

    """
    Functia creeaza o lista ce contine detaliile unei rezervari de zbor la o companie aeriana.
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: lista cu detaliile rezervarii.
    """

    return [id, nume, clasa, pret, checkin]


def getId(rezervare):

    """
    Functia returneaza id-ul unei rezervari.
    :param rezervare: dictionar ce contine detaliile unei rezervari.
    :return: id-ul rezervarii.
    """

    return rezervare[0]


def getNume(rezervare):

    """
    Functia returneaza numele pentru care s-a facut rezervarea.
    :param rezervare: dictionar ce contine detaliile unei rezervari.
    :return: numele unei rezervari.
    """

    return rezervare[1]


def getClasa(rezervare):

    """
    Functia returneaza clasa unei rezervari.
    :param rezervare: dictionar ce contine detaliile unei rezervari.
    :return: clasa unei rezervari.
    """

    return rezervare[2]


def getPret(rezervare):

    """
    Functia returneaza pretul unei calatorii.
    :param rezervare: dictionar ce contine detaliile unei rezervari.
    :return: pretul unei calatorii.
    """

    return rezervare[3]


def getCheckin(rezervare):

    """
    Functia returneaza "Da" daca persoana a facut check-in-ul, respectiv "Nu", in caz contrar.
    :param rezervare: dictionar ce contine detaliile unei rezervari.
    :return: "Da"/"Nu" (tip string)
    """

    return rezervare[4]


def getAll(rezervare):

    """
    Functia returenaza toate datele legate de rezervari.
    :param rezervare: dictionar ce contine detaliile unei rezervari.
    :return: datele rezervarilor (valorile cheilor).
    """

    return getId(rezervare), getNume(rezervare), getClasa(rezervare), getPret(rezervare), getCheckin(rezervare)


def toString(rezervare):

    """
    Functia converteste la string dictionarul.
    :param rezervare: dictionar cu detaliile uneor rezervari.
    :return: string.
    """

    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)

    )
