import unittest
from math_quiz import random_integer,random_operator,calculator


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
         operators=('+','-','*')
         for _ in range(1000):
              operator=random_operator()
              self.assertTrue(operator in operators)

    def test_calculator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 5, '*', '3 * 5',15),
                (2, 1, '-', '2 - 1',1),
                (5, 5, '+', '5 + 5',10)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                 problem,answer=calculator(num1,num2,operator)
                 self.assertTrue(problem==f"what is {expected_problem} ?" and answer==expected_answer)

if __name__ == "__main__":
    unittest.main()
