import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-2, -2)
        self.varasto3 = Varasto(10, 12)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, -1)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays_ei_muuta_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_taydella_varastolla_saldo_sama_kuin_tilavuus(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivisen_maaran_ottaminen_ei_muuta_mitaan(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-4)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_yli_saldon_ottaminen_ottaa_saldon_verran(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(11)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_nollaa_tilavuuden_negaatiivisella_arvolla(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_konstruktori_luo_tyhjan_varaston_negatiivisella_saldolla(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_konstruktori_luo_tayden_varaston_jos_alku_saldo_yli_tilavuuden(self):
        self.assertAlmostEqual(self.varasto3.saldo, self.varasto3.tilavuus)

    def test_str_metodi_palauttaa_oikean_merkkijonon(self):
        self.varasto.lisaa_varastoon(2)

        self.assertAlmostEqual(str(self.varasto), "saldo = 2, vielä tilaa 8")
