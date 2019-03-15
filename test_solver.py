from unittest import TestCase
from Solver import Solver


class TestSolver(TestCase):
    def test_calculate_iter1(self):
        s=Solver()
        self.assertTrue(s.calculate("")==[0])
    def test_calculate_iter2(self):
        s=Solver()
        self.assertTrue(s.calculate("4")==[1])
    def test_calculate_iter3(self):
        s=Solver()
        self.assertTrue(s.calculate("4,3")==[2])
    def test_calculate_iter4(self):
        s=Solver()
        self.assertTrue(s.calculate("4,3,6,7,8,9")==[6])