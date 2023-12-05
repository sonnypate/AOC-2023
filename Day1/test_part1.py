import pytest
import pathlib
import os
import day1


@pytest.fixture
def parent_directory():
    parent_dir = pathlib.Path(__file__).parent.resolve()
    return parent_dir


@pytest.fixture
def example1_input(parent_directory):
    script_path = os.path.join(parent_directory, 'example1.txt')
    return script_path


@pytest.fixture
def example2_input(parent_directory):
    script_path = os.path.join(parent_directory, 'example2.txt')
    return script_path


@pytest.fixture
def puzzle_input(parent_directory):
    script_path = os.path.join(parent_directory, 'puzzle_input.txt')
    return script_path


def test_get_example1_input(example1_input):
    """Test that the get_input function returns a list."""
    input_data = day1.get_input(example1_input)
    assert isinstance(input_data, list)


def test_get_example2_input(example2_input):
    """Test that the get_input function returns a list."""
    input_data = day1.get_input(example2_input)
    assert isinstance(input_data, list)


def test_solve_part1_example1_data(example1_input):
    """Example data should return 142."""
    input_data = day1.solve_part1(
        day1.get_input(example1_input))
    # https://adventofcode.com/2023/day/1 part 1 shows 142
    # as the sample data sum.
    assert input_data == 142, f"Input data received: {input_data}"


def test_convert_number_string():
    input_data = str("zoneight234")
    output_data = day1.convert_number_string(input_data)
    assert output_data == "zo1e8t234"


def test_solve_part2_example2_data(example2_input):
    """Example data should return 142."""
    input_data = day1.solve_part2(
        day1.get_input(example2_input))
    # https://adventofcode.com/2023/day/1 part 2 shows 281
    # as the sample data sum.
    assert input_data == 281, f"Input data received: {input_data}"
