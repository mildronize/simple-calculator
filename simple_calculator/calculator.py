# def add(num1, num2):
#     return num1 + num2
#

# 1+1
# 2
# 2+2
# 4
#    2-2
# 0

class Calculator():
    def __init__(self):
        print("Starting calculator.. ")
        self.operator = None


    # function -- split with '+'
    def split_by_plus(self, string):
        return string.split("+")

    def split_by_minus(self, string):
        return string.split("-")

    def convert_list_string_to_int(self, list_string):

        return [
            int(list_string[0]),
            int(list_string[1])
            ]

    # function -- convert to integer
    def calculate_list_int(self, list_int):
        if self.operator == "+":
            return list_int[0] + list_int[1]
        elif self.operator == "-":
            return list_int[0] - list_int[1]
        return None

    def define_operator(self, string):
        if "+" in string:
            self.operator = "+"
        elif "-" in string:
            self.operator = "-"
        return self.operator

    def calculate(self, string):

        split_result = self.split_by_plus(string)
        convert_result = self.convert_list_string_to_int(split_result)
        return self.calculate_list_int(convert_result)

if __name__ == '__main__':
    input_data = input("Enter your expression: ")
    print(Calculator().calculate(input_data))
