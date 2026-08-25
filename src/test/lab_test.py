import unittest

from src.main.character import Character
from src.main.lab import problem1


class LabTest(unittest.TestCase):
    def test_problem1_alphabetical_order(self):
        expected_list = [
            Character(3, "Jessica", "Atreides"),
            Character(1, "Leto", "Atreides"),
            Character(4, "Paul", "Atreides"),
            Character(5, "Feyd-Rautha", "Harkonnen"),
            Character(2, "Vladimir", "Harkonnen"),
        ]

        result_list = problem1()

        self.assertEqual(expected_list, result_list)


if __name__ == "__main__":
    unittest.main()
