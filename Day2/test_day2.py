import pytest
import pathlib
import os
import day2


@pytest.fixture
def parent_directory():
    parent_dir = pathlib.Path(__file__).parent.resolve()
    return parent_dir


@pytest.fixture
def example1_input(parent_directory):
    script_path = os.path.join(parent_directory, 'example1.txt')
    return script_path


@pytest.fixture
def puzzle_input(parent_directory):
    script_path = os.path.join(parent_directory, 'puzzle_input.txt')
    return script_path


def test_get_example1_input(example1_input):
    """Test that the get_input function returns a list."""
    input_data = day2.get_input(example1_input)
    assert isinstance(input_data, list)


def test_solve_part1_example1_data(example1_input):
    """Example data should return 8"""
    input_data = day2.solve_part1(
        day2.get_input(example1_input))
    # https://adventofcode.com/2023/day/2
    # Adding up game IDs 1, 2, and 5 = 8
    assert input_data == 8


def test_solve_part2_example1_data(example1_input):
    """Example data should return 2286"""
    input_data = day2.solve_part2(
        day2.get_input(example1_input))
    assert input_data == 2286


def test_get_game_id():
    """Test the the returned value is an int."""
    input_data = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    game_id = day2.get_game_id(input_data)
    assert isinstance(game_id, int)


def test_get_cube_counts():
    input_data = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    blue_cubes = day2.get_cube_count("blue", input_data)
    assert blue_cubes == ['6', '5']
