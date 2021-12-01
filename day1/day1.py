import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]

def part1(numbers):
    """Solve part 1"""
    # for num in numbers:
        # print(num) 

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        numbers = parse(puzzle_input)
        print(part1(numbers))