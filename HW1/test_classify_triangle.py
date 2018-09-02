from unittest import TestCase
from Tri import isnumber
from Tri import classify_triangle


class TestClassify_triangle(TestCase):
    def test_classify_equilateral(self):
        self.assertEqual("Equilateral ",classify_triangle(2,2,2), 'Should be Equilateral')


    def test_classify_isosceles(self):
        self.assertEqual("Isosceles ",classify_triangle(2,3,2),'Should be Isosceles')
        self.assertNotEqual(classify_triangle(10, 10, 10), 'Isoceles', 'Should be Equilateral')


    def test_classify_scalene(self):
        self.assertEqual("Scalene ",classify_triangle(2,3,24),'Should be only Scalene')


    def test_classify_right(self):
        self.assertEqual("Scalene Right",classify_triangle(4,3,5),'Should be Right Scalene')


    def test_classify_right(self):
        self.assertEqual("NotATriangle",classify_triangle(0,3,5),'Should be NotATriangle')

    def isnumber(self):
        self.assertEqual(True ,isnumber(2),'Should be True')