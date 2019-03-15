from unittest import TestCase
from Solver import Solver


class TestSolver(TestCase):
    def test_calculate(self):
        s=Solver()
        self.assertTrue(s.calculate("")=="")
