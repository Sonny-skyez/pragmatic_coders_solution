import sys
from typing import List


class ReversePolishNotation:
    """
    Class used to easily re-use this solution in other projects/applications.
    Use run_calculations function with proper string input to calculate the expression.
    """

    def __init__(self):
        self.math_operators = {
            "+": (lambda x, y: x + y),
            "-": (lambda x, y: x - y),
            "*": (lambda x, y: x * y),
            "/": (lambda x, y: x / y),
            "~": (lambda x, y: -y),
        }

    def input_data_validation(self, input_expression: str) -> List[str]:
        input_list = input_expression.split()
        for element in input_list:
            if element in self.math_operators:
                pass
            else:
                try:
                    validate_if_int = int(element)
                except Exception as ex:
                    sys.exit(
                        f"ERROR: Wrong input data format. Must be a string of integers & math operators: {ex}"
                    )

        return input_list

    def calculate_expression(self, input_elements: list) -> int:
        expression = self.check_if_calculation_or_negation(input_elements)
        stack_elements = list()
        for element in input_elements:
            if element in self.math_operators:
                argument_1 = (
                    stack_elements.pop(-2) if expression == "calculation" else None
                )
                argument_2 = stack_elements.pop(-1)
                result = self.math_operators[element](argument_1, argument_2)
                stack_elements.append(result)
            else:
                stack_elements.append(int(element))

        return stack_elements.pop()

    @staticmethod
    def check_if_calculation_or_negation(input_elements: list) -> str:
        if "~" not in input_elements:
            return "calculation"

    def run_calculations(self, input_expression: str) -> int:
        validated_input = self.input_data_validation(input_expression)
        if validated_input:
            result = self.calculate_expression(validated_input)
            return result
        else:
            print("Input mustn't be empty.")


onp = ReversePolishNotation()

result_1 = onp.run_calculations("")
result_x = onp.run_calculations("12 2 3 4 * 10 5 / + * +")
result_2 = onp.run_calculations("1 2 +")
result_3 = onp.run_calculations("4 2 / 3 *")
result_4 = onp.run_calculations("2 ~")
result_5 = onp.run_calculations("2 1 3 + +")

print(result_1, result_x, result_2, result_3, result_4)
