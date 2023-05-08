import unittest
from rearrange import rearrange_name
from compiler_letter import LetterCompiler

class TestModule(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_fail(self):
        testcase = "Lovelace, Ada"
        expected = "Ad Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_empty(self):
        testcase = ""
        expected = ""  
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_one_name(self):
        testcase = "Pedro"
        expected = "Pedro"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_compiler_letter(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)
