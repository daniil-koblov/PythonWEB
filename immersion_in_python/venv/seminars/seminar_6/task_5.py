from task_4 import questions
from random import choice


def play_puzzles(puzzles_data: dict[str, list[str]], count: int, tries: int) -> str:
    result = []
    while len(puzzles_data) and count:
        puzzle = choice(list(puzzles_data))
        answers = puzzles_data.pop(puzzle)
        puzzle_count = questions(puzzle, answers, tries)
        result.append(
            f'Загадка "{puzzle}"'
            + (
                f" отгадана с {puzzle_count} попытки"
                if puzzle_count
                else " не отгадана"
            )
        )
        count -= 1
    return "\n".join(result)


if __name__ == "__main__":
    puzzles = {
        "Ни лает, ни кусает, в дом не пускает?": ["замок", "сигнализация"],
        "Висит груша, нельзя скушать?": ["лампочка", "лампа"],
        "Зимой и летом одним цветом?": ["ель", "ёлка"],
    }
    print(play_puzzles(puzzles, 4, 3))