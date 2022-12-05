from typing import List


def test_data() -> List[str]:
    return [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]


def read_data() -> List[str]:
    with open("3/data.txt") as f:
        question_data = [x.rstrip("\n") for x in f.readlines()]
    return question_data


def find_common_value(strings: List[str]) -> str:
    output = ""
    common = set(strings[0])
    for i in range(len(strings[1:])):
        common = common.intersection(strings[i + 1])
    return "".join(common)


def numeric(values: List[str]):
    return sum(
        [
            ord(x.lower()) - 96 + 26 if x.lower() != x else ord(x.lower()) - 96
            for x in values
        ]
    )


def main():
    # data = test_data()
    data = read_data()
    split_strings = [[x[: len(x) // 2], x[len(x) // 2 :]] for x in data]
    groups_of_three = [data[x : x + 3] for x in range(0, len(data), 3)]
    values = [find_common_value(i) for i in split_strings]
    values_three = [find_common_value(i) for i in groups_of_three]
    print(numeric(values), numeric(values_three))


if __name__ == "__main__":
    main()
