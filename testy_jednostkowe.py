from unittest import TestCase


def suma(liczba1, liczba2):
    return liczba1 + liczba2


class Test(TestCase):

    def test_suma_test_1(self):
        expected = 5
        result = suma(2, 3)
        self.assertEqual(expected, result)

    def test_suma_test_2(self):
        expected = 7
        result = suma(2, 5)
        self.assertEqual(expected, result)

    def test_suma_error(self):
        with self.assertRaises(TypeError):
            suma("jff", 5)

    def test_suma_test_3(self):
        expected = -6
        result = suma(-3, -3)
        self.assertEqual(expected, result)
