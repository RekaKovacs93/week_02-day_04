import unittest
from src.task_decider import *

class TestTaskDecider (unittest.TestCase):
    def setUp(self):
        self.task1 = "wash_dishes"
        self.task2 = "clean_window"
        self.task3 = "cook_dinner"
        self.task4 = "do_ironing"
        self.task5 = "wash_clothes"

    def test_task_decider_one(self):
        self.assertEqual("wash_dishes", task_decider(self.task1,self.task2))

    def test_task_decider_two(self):
        self.assertEqual("wash_clothes", task_decider(self.task3,self.task5))

    def test_task_decider_three(self):
        self.assertEqual("do_ironing", task_decider(self.task4,self.task5))

    def test_task_decider_four(self):
        self.assertEqual("do_ironing", task_decider(self.task5,self.task4))

    def test_task_decider_five(self):
        self.assertEqual("clean_window", task_decider(self.task2,self.task2))




