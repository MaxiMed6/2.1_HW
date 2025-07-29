import unittest
from functions import sum_of_even_numbers, vowels_count, middle

#позитивные тест кейсы
class HomeworkTests(unittest.TestCase):
    def test_sum_of_even_numbers_positive(self):
        actual_result = sum_of_even_numbers(2, 4, 3, 7, 10)
        expected_result = 16

        self.assertEqual(expected_result, actual_result)

    def test_vowels_count_positive(self):
        actual_result = vowels_count("hello")
        expected_result = 2

        self.assertEqual(expected_result, actual_result)

    def test_middle_positive(self):
        actual_result = middle(5, 5, 5)
        expected_result = 5.0

        self.assertEqual(expected_result, actual_result)

    def test_vowels_count_upper_positive(self):
        actual_result = vowels_count("HELLO")
        expected_result = 2

        self.assertEqual(expected_result, actual_result)

    def test_sum_of_even__minus_numbers_positive(self):
        actual_result = sum_of_even_numbers(-2,-4, 3, 7, -10)
        expected_result = -16
        self.assertEqual(expected_result, actual_result)

#негативные тест кейсы
    def test_sum_of_even_numbers_none_negative(self):
        with self.assertRaises(TypeError):
            sum_of_even_numbers(None)

    def test_vowels_count_none_negative(self):
        with self.assertRaises(TypeError):
            vowels_count(None)

    def test_middle_empty_negative(self):
        with self.assertRaises(ZeroDivisionError):
            middle()

    def test_sum_of_even_numbers_invalid_negative(self):
        with self.assertRaises(TypeError):
            sum_of_even_numbers(1, "2", 3)

    def test_vowels_count_invalid_type_negative(self):
        with self.assertRaises(TypeError):
            vowels_count(123)





if __name__ == "__main__":
    unittest.main()