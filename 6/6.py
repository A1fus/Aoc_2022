from typing import Union


def test_data() -> str:
    return "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def read_data() -> str:
    with open("6/data.txt") as file:
        return file.read()


def find_signal(data: str, distinct_count: int) -> Union[int, str]:
    for window in range(len(data) - distinct_count):
        block = data[window : window + distinct_count]
        if len(set(block)) == distinct_count:
            return window + distinct_count
    return "No signal found"


def main():
    data = test_data()
    data = read_data()
    start_of_packet = find_signal(data, 4)
    start_of_message = find_signal(data, 14)
    print(start_of_packet, start_of_message)


if __name__ == "__main__":
    main()
