def creeazaRezervare(id, nume, clasa, pret, checkin):
    """
    Creeaza un dictionar pentru rezervarile unei companii aeriene.
    :param id: int
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: Dictionarul cu rezervarile companiei aeriene.
    """
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }

def getId(rezervare):
    """
    Ia id-ul unei rezervari.
    :param rezervare: Id-ul rezervarii.
    :return: Id-ul rezervarii.
    """
    return rezervare["id"]

def getNume(rezervare):
    '''
    Ia numele unei rezervari.
    :param rezervare: Dictionar ce retine o rezervare.
    :return: Numele rezervarii.
    '''
    return rezervare["nume"]

def getClasa(rezervare):
    '''
    Ia clasa unei rezervari.
    :param rezervare: Dictionar ce retine o rezervare.
    :return: Clasa rezervarii.
    '''
    return rezervare["clasa"]

def getPret(rezervare):
    '''
    Ia pretul unei calatorii.
    :param rezervare: Dictionar ce retine o rezervare.
    :return: Pretul calatoriei.
    '''
    return rezervare["pret"]

def getCheckin(rezervare):
    '''
    Ia starea de confirmare a calatoriei (DA/NU).
    :param rezervare: Dictionar ce retine o rezervare.
    :return: Starea de confirmare a calatoriei (DA/NU).
    '''
    return rezervare["checkin"]

def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )
