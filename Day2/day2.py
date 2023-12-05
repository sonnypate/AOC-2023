import pathlib
import sys
import re


def get_input(file) -> list:
    """Get the input data from a file and return a list."""
    path = pathlib.Path(file)
    input_data = path.read_text().strip()

    # Read data into list.
    return [str(line) for line in input_data.split("\n")]


def get_game_id(string: str) -> int:
    """Gets the game ID from the beginning of the string."""
    game_id = re.match(r"^Game (?P<GameID>\d+)", string)
    if game_id is None:
        return 0
    return int(game_id.group(1))


def get_cube_count(cube_color: str, input_data: str):
    """Gets the count of cubes for the specified color."""
    cube_count = re.findall(
        rf"(\d+)\s+{cube_color}+", input_data)
    return cube_count


def solve_part1(input_data: list[str]) -> int:
    """Solve part 1 of day 2."""
    # Total number of cubes for each color.
    total_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    # Used to sum all possible games together.
    possible_game_total = 0

    # for each game in the list provided.
    for game in input_data:
        game_id = get_game_id(game)
        red_cubes = get_cube_count("red", game)
        green_cubes = get_cube_count("green", game)
        blue_cubes = get_cube_count("blue", game)

        # Return true if this game can be possible.
        # The game can only be possible if all cube colors
        # are under the max.
        possible_game = True

        # If the provided cube count is greater
        # than the total cube count for that color,
        # then this game cannot be counted.
        for red_cube in red_cubes:
            if int(red_cube) > total_cubes["red"]:
                possible_game = False

        for green_cube in green_cubes:
            if int(green_cube) > total_cubes["green"]:
                possible_game = False

        for blue_cube in blue_cubes:
            if int(blue_cube) > total_cubes["blue"]:
                possible_game = False

        if possible_game:
            # Add the game ID to the total
            possible_game_total += game_id

    return possible_game_total


def solve_part2(input_data: list[str]) -> int:
    """Solve part 2 of day 2."""

    # Need to get the highest number of each cube color for each game.

    # Used to sum all possible games together.
    possible_game_total = 0

    # for each game in the list provided.
    for game in input_data:
        #game_id = get_game_id(game)
        red_cubes = get_cube_count("red", game)
        green_cubes = get_cube_count("green", game)
        blue_cubes = get_cube_count("blue", game)

        # Multiply the highest red, green, and blue cube numbers together.
        cube_power = 0

        # Convert the list of strings to list of ints.
        red_cube_ints = list(map(int, red_cubes))
        green_cube_ints = list(map(int, green_cubes))
        blue_cube_ints = list(map(int, blue_cubes))

        # Get the max value from each list.
        max_red_cube = max(red_cube_ints)
        max_green_cube = max(green_cube_ints)
        max_blue_cube = max(blue_cube_ints)

        # Get the cube power by multiplying the max colors together.
        cube_power = max_red_cube * max_green_cube * max_blue_cube

        # Then add the cube power to the game total.
        possible_game_total += cube_power

    return possible_game_total


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\nFile path: {path}")
        puzzle_input = path

        values = get_input(puzzle_input)
        print(f"Part 1 answer: {solve_part1(values)}")
        print(f"Part 2 answer: {solve_part2(values)}")
