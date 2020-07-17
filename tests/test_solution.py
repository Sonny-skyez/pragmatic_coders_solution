import pytest


input_value_1 = "12 2 3 4 * 10 5 / + * +"
result_value_1 = 40.0
input_value_2 = "4 2 /"
result_value_2 = 2.0
input_value_3 = "2 2 2 * *"
result_value_3 = 8
input_value_4 = " "
result_value_4 = None


@pytest.mark.parametrize(
    "input_string, output",
    [
        (input_value_1, result_value_1),
        (input_value_2, result_value_2),
        (input_value_3, result_value_3),
        (input_value_4, result_value_4),
    ],
)
def test_calculations_of_simple_and_complex_expressions(solution, input_string, output):
    assert solution.run_calculations(input_string) == output


input_a = "1 2 3 a + + +"
input_b = "@ 2 3 4 + - *"
output_validation = SystemExit


@pytest.mark.parametrize(
    "input_string, output", [(input_a, output_validation), (input_b, output_validation)]
)
def test_validation_of_input_strings_with_wrong_characters(
    solution, input_string, output
):

    with pytest.raises(SystemExit) as pytest_system_exit:
        assert solution.input_data_validation(input_string) == pytest_system_exit


input_c = "1 2 3 4 + + +"
input_d = "2 ~"
output_1 = "calculation"
output_2 = None


@pytest.mark.parametrize(
    "input_string, output", [(input_c, output_1), (input_d, output_2)]
)
def test_detection_of_calculation_and_negation_in_input_string(
    solution, input_string, output
):
    assert solution.check_if_calculation_or_negation(input_string) == output
