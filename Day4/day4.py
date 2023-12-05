import pathlib
import sys
import re


def get_input(file) -> list:
    """Get the input data from a file and return a list."""
    path = pathlib.Path(file)
    input_data = path.read_text().strip()

    # Read data into list.
    return [str(line) for line in input_data.split("\n")]


def get_card_id(string: str) -> int:
    """Gets the card ID from the beginning of the string."""
    card_id = re.match(r"^Card (?P<CardID>\d+)", string)
    if card_id is None:
        return 0
    return int(card_id.group(1))


def get_card_score(card_string: str) -> int:
    card_numbers = card_string.strip("Card ").lstrip('1234567890').strip(':').split('|')
    scratched_numbers = list(map(int, list(card_numbers[0].strip().split())))
    winning_numbers = list(map(int, list(card_numbers[1].strip().split())))

    score = 0
    # The score is done by doubling each matching number.
    # so if 4 are matching, then scoring is 1,2,4,8.
    for number in scratched_numbers:
        if number in winning_numbers:
            score += score
            if score == 0:
                score = 1
    
    return score


def solve_part1(input_data: list[str]) -> int:
    """Solve part 1 of day 4."""
    total_score = 0
    for card_string in input_data:
        total_score += get_card_score(card_string)
    return total_score


def solve_part2(input_data: list[str]) -> int:
    """Solve part 2 of day 4."""
    total_cards = input_data.__len__()
    pass


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\nFile path: {path}")
        puzzle_input = path

        values = get_input(puzzle_input)
        print(f"Part 1 answer: {solve_part1(values)}")
        print(f"Part 2 answer: {solve_part2(values)}")
