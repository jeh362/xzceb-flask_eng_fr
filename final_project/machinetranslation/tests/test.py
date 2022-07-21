import unittest
from translator import english_to_french
from translator import french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def testnull(self):
        self.assertNotEqual(english_to_french('None'),'')


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def testnull(self):
        self.assertNotEqual(french_to_english('None'),'')

unittest.main()