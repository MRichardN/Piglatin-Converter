import unittest
import latin_converter

class TestPiglatinConverter(unittest.TestCase):

  def test_starting_with_vowels(self):
  	self.assertEqual(latin_converter.piglatin_converter('andela'), 'andelaway')
  	
    

  def test_word_starting_with_consonant(self):
  	self.assertEqual(latin_converter.piglatin_converter('dog'), 'ogday')


  def test_word_containing_multiple_consonants_1(self):
  	self.assertEqual(latin_converter.piglatin_converter('trash'), 'ashtray')

  def test_word_containing_multiple_consonants_2(self):
  	self.assertEqual(latin_converter.piglatin_converter('system'), 'emsystay')   	
       



if __name__ =='__main__':
    unittest.main()


#Working Tests
  	#result = latin_converter.piglatin_converter('trash')
  	#expected = 'ashtray'
  	#self.assertEqual(expected, result)