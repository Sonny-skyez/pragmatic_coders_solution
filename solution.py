import sys


class ReversePolishNotation:
    """
    Class used to easily re-use this solution in other projects/applications.
    Use run_calculations function with proper string input to calculate the expression.
    """

    def __init__(self):
        self.input_elements = list()
        self.stack_elements = list()
        self.math_operators = {
            "+": (lambda x, y: x + y),
            "-": (lambda x, y: x - y),
            "*": (lambda x, y: x * y),
            "/": (lambda x, y: x / y),
            "~": (lambda x, y: -x),
        }

    def input_data_validation(self, input_expression: str):
        input_list = list(input_expression)
        for element in input_list:
            if element == " ":
                input_list.remove(element)
            elif element in self.math_operators:
                pass
            else:
                try:
                    validate_if_int = int(element)
                except Exception as ex:
                    print(
                        f"ERROR: Wrong input data format. Must be a string of integers & math operators: {ex}"
                    )
                    sys.exit()

        return input_list

    @staticmethod
    def check_if_the_data_is_valid_and_input_is_a_proper_list(input_expression: list):
        if type(input_expression) == list:
            return input_expression

    def calculate_expression(self, input_elements: list):
        expression = self.check_if_calculation_or_negation(input_elements)
        for element in input_elements:
            if element in self.math_operators:
                argument_1 = self.stack_elements.pop()
                argument_2 = (
                    self.stack_elements.pop() if expression == "calculation" else 0
                )
                result = self.math_operators[element](argument_1, argument_2)
                self.stack_elements.append(result)
            else:
                self.stack_elements.append(int(element))

        return self.stack_elements.pop()

    @staticmethod
    def check_if_calculation_or_negation(input_elements: list):
        if "~" not in input_elements:
            return "calculation"

    def run_calculations(self, input_expression: str):
        validated_input = self.input_data_validation(input_expression)
        self.input_elements = self.check_if_the_data_is_valid_and_input_is_a_proper_list(
            validated_input
        )
        if self.input_elements:
            result = self.calculate_expression(self.input_elements)
            return result
        else:
            print("Input mustn't be empty.")


onp = ReversePolishNotation()

result_1 = onp.run_calculations("")
result_2 = onp.run_calculations("1 2 +")
result_3 = onp.run_calculations("4 2 / 3 *")
result_4 = onp.run_calculations("2 ~")

print(result_1, result_2, result_3, result_4)
