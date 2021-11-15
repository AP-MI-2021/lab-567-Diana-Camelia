from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare, testModificareClasa
from Tests.testConsola import testUndoRedo
from Tests.testDomain import testRezervare
from Tests.testFunctionalitati import testIeftiniri, testDeterminarePretMaximClasa, testOrdonare, \
    testAfisareSumaPreturilorFiecareNume


def testAll():
    """
    Functia apeleaza toate testele facute in parte.
    """
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testIeftiniri()
    testModificareClasa()
    testDeterminarePretMaximClasa()
    testOrdonare()
    testAfisareSumaPreturilorFiecareNume()
    testUndoRedo()