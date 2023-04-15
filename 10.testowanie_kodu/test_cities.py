import unittest

from main import city_country

class CityCountryCase(unittest.TestCase):
    
    def test_city_country(self):
        formatted_city_country = city_country('katowice', 'polska')
        self.assertEqual(formatted_city_country, 'Katowice, Polska')
        
    def test_city_country_population(self):
        formatted_city_country = city_country('katowice', 'polska', 50000000)
        self.assertEqual(formatted_city_country, 'Katowice, Polska - Populacja 50000000')
if __name__ == '__main__':
    unittest.main()