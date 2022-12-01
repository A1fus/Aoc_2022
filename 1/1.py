from typing import List
from data import data


def sample_data() -> List[List[int]]:
    return [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]


def total_cals(list_of_cals: List[List[int]]) -> List[int]:
    return [sum(x) for x in list_of_cals]


def max_cals(total_cals: List[int]) -> int:
    return max(total_cals)


def max_3_cals(total_cals: List[int]) -> int:
    return sum(sorted(total_cals)[-3:])


def main():
    list_of_cals = data
    list_total_cals = total_cals(list_of_cals)
    print(max_cals(list_total_cals), max_3_cals(list_total_cals))


if __name__ == "__main__":
    main()
