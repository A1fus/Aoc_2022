from typing import List
import re


def test_data() -> List[str]:
    return ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]


def read_data() -> List[str]:
    with open("4/data.txt") as f:
        return [x.rstrip("\n") for x in f.readlines()]


def parse_data(data: List[str]) -> List[List[int]]:
    return [[int(x) for x in lst] for lst in [re.findall(r"\d+", x) for x in data]]


def count_subsets(data: List[List[int]]) -> int:
    count = 0
    for x in data:
        if (x[0] >= x[2] and x[1] <= x[3]) or (x[2] >= x[0] and x[3] <= x[1]):
            count += 1
    return count


def count_overlaps(data: List[List[int]]) -> int:
    count = 0
    for x in data:
        if x[1] >= x[2] and x[0] <= x[3]:
            count += 1
    return count


def main():
    data = test_data()
    data = read_data()
    parsed = parse_data(data)
    print(count_subsets(parsed), count_overlaps(parsed))


if __name__ == "__main__":
    main()
