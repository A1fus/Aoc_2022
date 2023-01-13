from typing import List
from copy import deepcopy


def test_data() -> List[List[int]]:
    return [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


def read_data():
    with open("8/data.txt") as file:
        return [[int(x) for x in line.rstrip("\n")] for line in file.readlines()]


def check_horizontal(row, tree_index, tree, visible_trees):
    visible_trees = deepcopy(visible_trees)
    if (
        len(
            [
                blocking_tree
                for blocking_tree in row[: tree_index + 1]
                if blocking_tree >= tree
            ]
        )
        == 0
    ) or (
        len(
            [
                blocking_tree
                for blocking_tree in row[tree_index + 2 :]
                if blocking_tree >= tree
            ]
        )
        == 0
    ):
        visible_trees.append(tree)
    return visible_trees


def check_vertical(data, row_index, tree_index, tree, visible_trees):
    visible_trees = deepcopy(visible_trees)
    trees_above_below = [trees[tree_index + 1] for trees in data[: row_index + 1]]
    trees_below= [
        trees[tree_index + 1] for trees in data[row_index + 2 :]
    ]
    if (
        len(
            [
                blocking_tree
                for blocking_tree in trees_above_below
                if blocking_tree >= tree
            ]
        )
        == 0
    ) or (
        len(
            [
                blocking_tree
                for blocking_tree in trees_below
                if blocking_tree >= tree
            ]
        )
        == 0
    ):
        visible_trees.append(tree)
    return visible_trees


def find_visible_trees(data):
    visible_trees = []
    for row_index, row in enumerate(data[1:-1]):
        for tree_index, tree in enumerate(row[1:-1]):
            count_visible = len(visible_trees)
            visible_trees = check_horizontal(row, tree_index, tree, visible_trees)
            # if len(visible_trees) != count_visible:
            #     continue
            visible_trees = check_vertical(
                data, row_index, tree_index, tree, visible_trees
            )
    return visible_trees


def main():
    data = test_data()
    data = read_data()
    # print(data)
    visible_trees = find_visible_trees(data)
    print(len(visible_trees) + len(data[1:-1])*2 + len(data)*2)


if __name__ == "__main__":
    main()
