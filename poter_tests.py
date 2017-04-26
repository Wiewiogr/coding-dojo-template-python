import unittest
from basket import Basket


class ExampleTest(unittest.TestCase):
    def test_price_for_empty_basket(self):
        basket = Basket()
        price = basket.getPrice()
        self.assertEqual(0, price)

    def test_price_for_one_book(self):
        basket = Basket()
        basket.addBook("Pierwsza")
        price = basket.getPrice()
        self.assertEqual(100, price)

    def test_price_for_two_same_book(self):
        basket = Basket()
        basket.addBook("Pierwsza")
        basket.addBook("Pierwsza")
        price = basket.getPrice()
        self.assertEqual(200, price)

    def test_price_for_three_same_book(self):
        basket = Basket()
        basket.addBook("Pierwsza")
        basket.addBook("Pierwsza")
        basket.addBook("Pierwsza")
        price = basket.getPrice()
        self.assertEqual(300, price)

    def test_price_for_two_different_books(self):
        basket = Basket()
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        price = basket.getPrice()
        self.assertEqual(190, price)

    def test_price_for_three_different_books(self):
        basket = Basket()
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        basket.addBook("Trzecia")
        price = basket.getPrice()
        self.assertEqual(270, price)

    def test_price_for_four_different_books(self):
        basket = Basket()
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        basket.addBook("Trzecia")
        basket.addBook("Czwarta")
        price = basket.getPrice()
        self.assertEqual(320, price)

    def test_price_for_five_different_books(self):
        basket = Basket()
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        basket.addBook("Trzecia")
        basket.addBook("Czwarta")
        basket.addBook("Piata")
        price = basket.getPrice()
        self.assertEqual(375, price)

    def test_price_for_two_same_books_and_one_different(self):
        basket = Basket()
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        basket.addBook("Pierwsza")
        price = basket.getPrice()
        self.assertEqual(290, price)

    def test_price_for_two_different_books_doubled(self):
        basket = Basket()
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        price = basket.getPrice()
        self.assertEqual(380, price)

    def test_price_for_five_different_books_doubled(self):
        basket = Basket()
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        basket.addBook("Trzecia")
        basket.addBook("Czwarta")
        basket.addBook("Piata")
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        basket.addBook("Trzecia")
        basket.addBook("Czwarta")
        basket.addBook("Piata")
        price = basket.getPrice()
        self.assertEqual(875, price)

    def test_price_sample_order(self):
        basket = Basket()
        basket.pricePerBook = 8
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        basket.addBook("Trzecia")
        basket.addBook("Czwarta")
        basket.addBook("Piata")
        basket.addBook("Pierwsza")
        basket.addBook("Druga")
        basket.addBook("Trzecia")
        price = basket.getPrice()
        self.assertEqual(51.2, price)

if __name__ == '__main__':
    unittest.main()
