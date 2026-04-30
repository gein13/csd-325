#Scott Chamberlain
#4/30/2026
#M7.2 Assignment

import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        """Test that city and country are formatted correctly."""
        result = city_country("Toronto", "Canada")
        self.assertEqual(result, "Toronto, Canada")


if __name__ == "__main__":
    unittest.main()