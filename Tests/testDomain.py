from Domain.rezervare import creeazaRezervare, getId, getClasa, getNume, getPret, getCheckin, getAll


def testRezervare():
    rezervare = creeazaRezervare("1", "Marcel", "business", 1000, "Da")
    assert getId(rezervare) == "1"
    assert getNume(rezervare) == "Marcel"
    assert getClasa(rezervare) == "business"
    assert getPret(rezervare) == 1000
    assert getCheckin(rezervare) == "Da"
    assert getAll(rezervare) == ("1", "Marcel", "business", 1000, "Da")

    id, nume, clasa, pret, checkin = getAll(rezervare)
    assert id == "1"
    assert clasa == "business"
    assert checkin == "Da"

