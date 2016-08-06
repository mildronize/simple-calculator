import unittest

from simple_calculator.calculator import Calculator

# class AddTest(unittest.TestCase):
#
#     def add_1_1_should_be_2_test(self):
#         self.assertEqual( add(1,1), 2)


class SplitByPlusTest(unittest.TestCase):

    def split_1_plus_1_should_be_list_of_1_1_test(self):
        assert Calculator().split_by_plus("1+1") == ['1','1']
        # self.assertEqual( Calculator().split_by_plus("1+1"), ['1','1'])

    def split_3_plus_5_should_be_list_of_3_5_test(self):
        self.assertEqual( Calculator().split_by_plus("3+5"), ['3','5'])

    def split_1_plus_2_should_be_list_of_1_2_test(self):
        self.assertEqual( Calculator().split_by_plus("1+2"), ['1','2'])

class ConvertListStringToIntTest(unittest.TestCase):

    def convert_list_of_1_1_string_to_1_1_int_test(self):
        self.assertEqual( Calculator().convert_list_string_to_int(['1','1']), [1,1])

class CalculateListIntTest(unittest.TestCase):
    def calculate_list_of_1_1_int_should_be_2_test(self):
        c = Calculator()
        c.define_operator("1+1")
        self.assertEqual( c.calculate_list_int([1,1]), 2)

class CalculateTest(unittest.TestCase):
    def calculate_string_1_plus_1_should_be_2_test(self):
        self.assertEqual( Calculator().calculate("1+1"), 2)

class DefineOperatorTest(unittest.TestCase):
    def define_operator_1_plus_1_should_be_plus_test(self):
        self.assertEqual( Calculator().define_operator("1+1"), "+")

    def define_operator_1_minus_1_should_be_minus_test(self):
        self.assertEqual( Calculator().define_operator("1-1"), "-")

    def define_operator_1_1_should_be_none_test(self):
        self.assertEqual( Calculator().define_operator("11"), None)
