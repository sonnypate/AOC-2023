import pathlib
import sys


def get_input(file) -> list:
    """Get the input data from a file and return a list."""
    path = pathlib.Path(file)
    input_data = path.read_text().strip()

    # Read data into list.
    return [str(line) for line in input_data.split()]


def convert_number_string(input_data: str) -> str:
    """Convert spelled numbers to regular numbers."""

    # Translation dictionary for conversion.
    spelled_numbers = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    # Modify the output data in each iteration,
    # by storing it outside the loop.
    output_data = input_data

    # If the key from the spelled_numbers dictionary
    # is found in the string, replace it with the value.
    for k, v in spelled_numbers.items():
        if k in input_data:
            output_data = output_data.replace(k, v)

    return output_data


def solve_part1(input_data: list[str]) -> int:
    """Parse each string in list to pull the first and last number."""

    calibration_total = 0

    for calibration_string in input_data:

        numbers_found = []

        # Each character of the calibration value
        # needs to be tested to see if it's numeric.
        for char in calibration_string:
            if char.isnumeric():
                numbers_found.append(char)

        # Create a string based on the first and last numbers
        # of the list concatinated together.
        calibration_value_string = f"{numbers_found[0]}{numbers_found[-1]}"

        # Need to add these numbers, so this needs to be converted to an int.
        # Then add that value to the calibration_total to return it after
        # all lines have been parsed.
        calibration_value_int = int(calibration_value_string)
        calibration_total += calibration_value_int

    return calibration_total


def solve_part2(input_data: list[str]) -> int:
    """Same as part1 but with the string conversions needed in part2."""

    calibration_total = 0

    for calibration_string in input_data:

        # First convert the calibration strings to work with
        # the new requirements, then process the same as part 1.
        converted_calibration_string = convert_number_string(
            calibration_string
            )

        numbers_found = []

        # Each character of the calibration value
        # needs to be tested to see if it's numeric.
        for char in converted_calibration_string:
            if char.isnumeric():
                numbers_found.append(char)

        # Create a string based on the first and last numbers
        # of the list concatinated together.
        calibration_value_string = f"{numbers_found[0]}{numbers_found[-1]}"

        # Need to add these numbers, so this needs to be converted to an int.
        # Then add that value to the calibration_total to return it after
        # all lines have been parsed.
        calibration_value_int = int(calibration_value_string)
        calibration_total += calibration_value_int

    return calibration_total


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\nFile path: {path}:")
        puzzle_input = path

        values = get_input(puzzle_input)
        print(f"Part 1 answer: {solve_part1(values)}")
        print(f"Part 2 answer: {solve_part2(values)}")
