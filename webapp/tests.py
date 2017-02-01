from django.test import TestCase
import roman_arithematic as ra
import unittest

class TestMyFunctions(unittest.TestCase):
    def test_Int_to_roman(self):
            a = 66
            expected = "LXVI"
            actual = ra.int_to_roman(a)
            self.assertEqual(expected, actual, "failed test for int to roman")
            
    """ failue case check"""
    def test_Int_to_roman(self):
            a = 67
            expected = "LXVI"
            actual = ra.int_to_roman(a)
            self.assertEqual(expected, actual, "failed test for int to roman")

    def test_Roman_to_int(self):
            a = "LXVI"
            expected = 66
            actual = ra.roman_to_int(a)
            self.assertEqual(expected, actual, "Failed test for roman to int")
                
    def test_roman_arithematic_operation(self):
            a = "V"
            b = "VI"
            operator = "+"
            expected = "XI"
            actual = ra.roman_arithematic_operation(a,b,operator)
            self.assertEqual(expected, actual, "Failed test for arithematic operation")
            
if __name__ == '__main__':
	unittest.main()
