import pytest
import pathlib
import os
import day4


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
    input_data = day4.get_input(example1_input)
    assert isinstance(input_data, list)


def test_solve_part1_example1_data(example1_input):
    """Example data should return 8"""
    input_data = day4.solve_part1(
        day4.get_input(example1_input))
    # https://adventofcode.com/2023/day/4
    assert input_data == 13


def test_solve_part2_example1_data(example1_input):
    """Example data should return 30"""
    input_data = day4.solve_part2(
        day4.get_input(example1_input))
    assert input_data == 30


def test_get_card_score():
    """Example card should return 2"""
    example_card = "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"
    input_data = day4.get_card_score(example_card)
    assert input_data == 2


def test_get_card_id():
    """Example card should return 1 for the card ID"""
    example_card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    input_data = day4.get_card_id(example_card)
    assert input_data == 1