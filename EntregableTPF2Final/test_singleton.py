import unittest
from corporate_data import CorporateData
from corporate_log import CorporateLog

class TestSingletonPattern(unittest.TestCase):

    def test_corporate_data_singleton(self):
        # Crear dos instancias de CorporateData
        instance1 = CorporateData()
        instance2 = CorporateData()
        # Comprobar que ambas instancias son iguales
        self.assertIs(instance1, instance2, "CorporateData no está implementado como Singleton")

    def test_corporate_log_singleton(self):
        # Crear dos instancias de CorporateLog
        instance1 = CorporateLog()
        instance2 = CorporateLog()
        # Comprobar que ambas instancias son iguales
        self.assertIs(instance1, instance2, "CorporateLog no está implementado como Singleton")

    def test_corporate_data_consistent_attributes(self):
        # Probar consistencia de atributos en CorporateData
        instance1 = CorporateData()
        instance2 = CorporateData()
        instance1.some_attribute = "test_value"
        self.assertEqual(instance2.some_attribute, "test_value", "Atributos inconsistentes en CorporateData Singleton")

    def test_corporate_log_consistent_attributes(self):
        # Probar consistencia de atributos en CorporateLog
        instance1 = CorporateLog()
        instance2 = CorporateLog()
        instance1.some_attribute = "test_value"
        self.assertEqual(instance2.some_attribute, "test_value", "Atributos inconsistentes en CorporateLog Singleton")

if __name__ == "__main__":
    unittest.main()
