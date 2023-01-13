from typing import List, Dict, Union
import re
import copy


def test_data() -> List[str]:
    return [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]


def dirs(data: List[str]) -> List[str]:
    return re.findall(r"\$ cd \w", "|".join(data))


def ls(data: List[str], directory: str):
    ls_index = data.index(directory) + 2
    output = []
    for line in data[ls_index:]:
        if line[0] == "$" or data[-1] == line:
            return output
        output.append(line)


def format_data(data: List[str]) -> Dict[str, List[str]]:
    directories = dirs(data)
    ls_output = {}
    for directory in directories:
        ls_output[directory] = ls(data, directory)
    return ls_output


def total_directory_size(directories: Dict[str, List[str]]):
    return {
        dir: sum(int(size) for size in re.findall(r"\d+", "|".join(files)))
        for dir, files in directories.items()
    }, {
        dir: [x for x in re.findall(r"dir \w", "|".join(files))]
        for dir, files in directories.items()
    }

def add_on_subdirs(directories, subdirs_map):
    directories = copy.deepcopy(directories)
    for dir, subdirs in subdirs_map.items():
        for subdir in subdirs:
            directories[dir] = directories[dir] + directories[subdir]
    return directories

def sum_directories_below_target(
    directories: Dict[str, int], target: int
) -> int:
    return sum(size for dir, size in directories.items() if size <= target)


def main():
    data = test_data()
    # print(data)
    formatted = format_data(data)
    print(formatted)
    directory_sizes, subdirs = total_directory_size(formatted)
    # print(formatted)
    # print(directory_sizes,subdirs)
    final_directory_sizes = add_on_subdirs(directory_sizes, subdirs)
    print(sum_directories_below_target(final_directory_sizes, 100000))


if __name__ == "__main__":
    main()
