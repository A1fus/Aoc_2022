from typing import List
import copy


def test_data() -> List[List[str]]:
    return [["A", "Y"], ["B", "X"], ["C", "Z"]]


def read_data() -> List[List[str]]:
    with open("2/data.txt") as f:
        question_data = [[x[0], x[2]] for x in f.readlines()]
    return question_data


def convert_to_scores(data: List[List[str]]) -> List[List[int]]:
    score_mapping = {"X": 1, "Y": 2, "Z": 3}
    opponent_mapping = {"A": 1, "B": 2, "C": 3}
    return [[opponent_mapping[x], score_mapping[y]] for x, y in data]


def score(data: List[List[int]]) -> int:
    player_score = 0
    for x in data:
        player_score += x[1]
        if x[0] == x[1]:
            player_score += 3
        elif (
            (x[0] == 1 and x[1] == 2)
            or (x[0] == 2 and x[1] == 3)
            or (x[0] == 3 and x[1] == 1)
        ):
            player_score += 6
    return player_score


def apply_rules(data: List[List[int]]) -> List[List[int]]:
    lose_map = {1: 3, 2: 1, 3: 2}
    win_map = {1: 2, 2: 3, 3: 1}
    data = copy.deepcopy(data)
    for x in data:
        if x[1] == 1:
            x[1] = lose_map[x[0]]
        elif x[1] == 2:
            x[1] = x[0]
        elif x[1] == 3:
            x[1] = win_map[x[0]]
    return data


def main():
    data = read_data()
    # data = test_data()
    int_data = convert_to_scores(data)
    rules_data = apply_rules(int_data)
    print(score(int_data), score(rules_data))


if __name__ == "__main__":
    main()
