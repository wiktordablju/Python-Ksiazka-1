import unittest
from main import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.myself = Employee('Wiktor', 'Dziendziel', 20000)
        
    def test_give_raise_default(self):
        self.myself.give_raise()
        answer = self.myself.show_employee()
        self.assertEqual(answer, 'Imie - Wiktor\nNazwisko - Dziendziel\nZarobki - 25000')
    
    def test_give_raise_custom(self):
        self.myself.give_raise(10000)
        answer = self.myself.show_employee()
        self.assertEqual(answer, 'Imie - Wiktor\nNazwisko - Dziendziel\nZarobki - 30000')
    
        
if __name__ == '__main__':
    unittest.main()