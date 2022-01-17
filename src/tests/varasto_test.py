import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_ei_alle_nollan(self):
        nolla_varasto = Varasto(-2, 0)

        self.assertAlmostEqual(nolla_varasto.tilavuus, 0)
        

    def test_saldo_ei_alle_nollan(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(40)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_saldo_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(500)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_alle_nollan_lisaaminen_ei_muuta(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_alle_nollan_ottaminen_ei_vaikuta(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(-6)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_saldo_alle_nollan_menee_nollaan(self):
        testi_varasto = Varasto(10, -5)

        self.assertAlmostEqual(testi_varasto.saldo, 0)

    def test_to_string_antaa_oikeat_arvot(self):
        self.varasto.lisaa_varastoon(5)

        varasto2 = Varasto(10)

        varasto2.lisaa_varastoon(5)

        self.assertTrue(str(self.varasto) == str(varasto2))
        

        