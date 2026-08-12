from django.test import TestCase

class TesteBasico(TestCase):
    
    def test_matematica_simples(self):
        self.assertEqual(1+1, 2)
