"""Unit tests for the MustangBronco program

This module is used to test the MustangBronco implementation. 

  Typical usage example:
  # From project directory
  python -m mustang_bronco.tests.mustang_bronco_test -v
"""

import unittest
from mustang_bronco.src.mustang_bronco import mustang_bronco

class TestMustangBronco(unittest.TestCase):

  def test_mustang(self):
    self.assertEqual(mustang_bronco(3), 'Mustang')
    self.assertEqual(mustang_bronco(6), 'Mustang')
    self.assertEqual(mustang_bronco(9), 'Mustang')
    self.assertEqual(mustang_bronco(12), 'Mustang')
    self.assertEqual(mustang_bronco(18), 'Mustang')
    self.assertEqual(mustang_bronco(21), 'Mustang')
  
  def test_bronco(self):
    self.assertEqual(mustang_bronco(5), 'Bronco')
    self.assertEqual(mustang_bronco(10), 'Bronco')
    self.assertEqual(mustang_bronco(20), 'Bronco')
    self.assertEqual(mustang_bronco(25), 'Bronco')
    self.assertEqual(mustang_bronco(35), 'Bronco')
    self.assertEqual(mustang_bronco(40), 'Bronco')

  def test_mustang_bronco(self):
    self.assertEqual(mustang_bronco(0), 'MustangBronco')
    self.assertEqual(mustang_bronco(15), 'MustangBronco')
    self.assertEqual(mustang_bronco(30), 'MustangBronco')
    self.assertEqual(mustang_bronco(45), 'MustangBronco')
    self.assertEqual(mustang_bronco(60), 'MustangBronco')
    self.assertEqual(mustang_bronco(75), 'MustangBronco')
  
  def test_non(self):
    self.assertEqual(mustang_bronco(1), '1')
    self.assertEqual(mustang_bronco(2), '2')
    self.assertEqual(mustang_bronco(4), '4')
    self.assertEqual(mustang_bronco(7), '7')
    self.assertEqual(mustang_bronco(11), '11')
    self.assertEqual(mustang_bronco(13), '13')

if __name__ == '__main__':
  unittest.main()