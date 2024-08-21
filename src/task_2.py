from collections import Counter


def count_elements(elements: list[list]) -> list[list]:
    counter = Counter(map(tuple, elements))
    result = [[*i[0], i[1]] for i in counter.items()]

    return result


def main() -> None:
    list_version = [
        ["665587", 2],
        ["669532", 1],
        ["669537", 2],
        ["669532", 1],
        ["665587", 1],
    ]
    result = count_elements(list_version)
    print(result)


if __name__ == "__main__":
    main()
