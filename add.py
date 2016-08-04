# def add(num1, num2):
#     return num1 + num2
#

# 1+1
# 2
# 2+2
# 4

# function -- split with '+'
def split_by_plus(string):
    return string.split("+")

def convert_list_string_to_int(list_string):

    return [
        int(list_string[0]),
        int(list_string[1])
        ]

# function -- convert to integer
def calculate_list_int(list_int):
    return list_int[0] + list_int[1]

def calculate(string):
    a = split_by_plus(string)
    b = convert_list_string_to_int(a)
    return calculate_list_int(b)

if __name__ == '__main__':
    input_data = input("Enter your expression: ")
    print(calculate(input_data))
