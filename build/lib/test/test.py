import unittest
from matematika import operasi, hello

class TestMatematika(unittest.TestCase):

    def test_penjumlahan(self):
        result = operasi.penjumlahan(3, 3)
        self.assertEqual(result, 6)

    def test_pengurangan(self):
        result = operasi.pengurangan(5, 2)
        self.assertEqual(result, 3)

    def test_perkalian(self):
        result = operasi.perkalian(3, 3)
        self.assertEqual(result, 9)

    def test_pembagian(self):
        result = operasi.pembagian(12, 3)
        self.assertEqual(result, 4)

    def test_hello(self):
        result = hello.hello()
        self.assertEqual(result, "Hello World!")

if __name__ == '__main__':
    unittest.main()