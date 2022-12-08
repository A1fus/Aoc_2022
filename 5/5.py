from typing import List, Dict
from copy import deepcopy
import re


def test_setup() -> List[str]:
    return ["    [D]   ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 "]


def test_instructions() -> List[str]:
    return [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]


def read_setup() -> List[str]:
    with open("5/data.txt") as f:
        return [line.rstrip("\n") for line in f.readlines()]


def read_instructions() -> List[str]:
    with open("5/instructions.txt") as f:
        return [line.rstrip("\n") for line in f.readlines()]


def parse_row(
    stacks: Dict[str, List[str]], row: str, bays: List[str], stack_indexes: List[int]
) -> None:
    for bay, index in zip(bays, stack_indexes):
        if row[index] != " ":
            stacks[bay].append(row[index])


def parse_setup(setup: List[str]) -> Dict[str, List[str]]:
    setup = deepcopy(setup)
    stacks = list(setup[-1])
    bays = list(filter(lambda bay: bay != " ", stacks))
    stack_indexes = [stacks.index(stack) for stack in bays]
    stacks = {bay: [] for bay in bays}
    for row in setup[:-1]:
        parse_row(stacks=stacks, row=row, bays=bays, stack_indexes=stack_indexes)
    for bay in bays:
        stacks[bay].reverse()
    return stacks


def parse_instructions(instructions: List[str]) -> List[List[str]]:
    return [re.findall(r"\d+", x) for x in instructions]


def apply_instruction(
    stacks: Dict[str, List[str]], instruction: List[str], first_part: bool = True
) -> Dict[str, List[str]]:
    holding = []
    stacks = deepcopy(stacks)
    count, from_stack, to_stack = int(instruction[0]), instruction[1], instruction[2]
    holding = stacks[from_stack][-count:]
    if first_part:
        holding.reverse()
    stacks[from_stack] = stacks[from_stack][:-count]
    stacks[to_stack] = stacks[to_stack] + holding
    return stacks


def apply_instructions(
    stacks: Dict[str, List[str]], instructions: List[List[str]], first_part: bool = True
) -> Dict[str, List[str]]:
    for instruction in instructions:
        stacks = apply_instruction(stacks, instruction, first_part)
    return stacks


def main():
    setup = test_setup()
    setup = read_setup()
    stacks = parse_setup(setup)
    instructions = test_instructions()
    instructions = read_instructions()
    parsed_instructions = parse_instructions(instructions)
    stacks_first = apply_instructions(stacks, parsed_instructions)
    stacks_second = apply_instructions(stacks, parsed_instructions, first_part=False)
    output_first = "".join([stack[-1] for stack in stacks_first.values()])
    output_second = "".join([stack[-1] for stack in stacks_second.values()])
    print(output_first, output_second)


if __name__ == "__main__":
    main()
