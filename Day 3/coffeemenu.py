import unittest

class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }


class TestCoffeeMenu(unittest.TestCase):
     def setUp(self):
        self.menu = CoffeeMenu()
     def tearDown(self):
        self.menu = None
     def test_get_price_existing_item(self):
        self.assertEqual(self.menu.menu['latte'], 2.75)
     
     def test_add_items(self):
        self.menu.menu['mocha'] = 3.50
        self.assertIn('mocha', self.menu.menu)
        self.assertEqual(self.menu.menu['mocha'], 3.50)

if __name__ == "__main__":
    unittest.main()