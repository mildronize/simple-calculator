import unittest
from add import *

# class AddTest(unittest.TestCase):
#
#     def add_1_1_should_be_2_test(self):
#         self.assertEqual( add(1,1), 2)


class SplitByPlusTest(unittest.TestCase):

    def split_1_plus_1_should_be_list_of_1_1_test(self):
        self.assertEqual( split_by_plus("1+1"), ['1','1'])

    def split_3_plus_5_should_be_list_of_3_5_test(self):
        self.assertEqual( split_by_plus("3+5"), ['3','5'])

    def split_1_plus_2_should_be_list_of_1_2_test(self):
        self.assertEqual( split_by_plus("1+2"), ['1','2'])

class ConvertListStringToIntTest(unittest.TestCase):

    def convert_list_of_1_1_string_to_1_1_int_test(self):
        self.assertEqual( convert_list_string_to_int(['1','1']), [1,1])

class CalculateListIntTest(unittest.TestCase):
    def calculate_list_of_1_1_int_should_be_2_test(self):
        self.assertEqual( calculate_list_int([1,1]), 2)

class CalculateTest(unittest.TestCase):
    def calculate_string_1_plus_1_should_be_2_test(self):
        self.assertEqual( calculate("1+1"), 2)
