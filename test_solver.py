from unittest import TestCase
from Solver import Solver


class TestSolver(TestCase):
    def test_calculate_iter1(self):
        s=Solver()
        self.assertTrue(s.calculate("")==[0,0,0,0])
    def test_calculate_iter2(self):
        s=Solver()
        self.assertTrue(s.calculate("1,2,3,4,5")==[5,1,5,3])