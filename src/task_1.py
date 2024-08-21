import re

LIST_KEYS = [
    "name",
    "day_month",
    "day_of_week",
    "start_time",
    "end_time",
    "master",
    "services",
]


def validate_text(text: str) -> str:
    open_braces = [match.start() for match in re.finditer("{", text)]
    close_braces = [match.end() for match in re.finditer("}", text)]

    if len(open_braces) != len(close_braces):
        raise NameError

    for start, end in zip(open_braces, close_braces):
        if text[start:end] not in LIST_KEYS:
            raise NameError

    return text


def main() -> None:
    Test_text = """{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}"""

    result = validate_text(Test_text)
    print(result)


if __name__ == "__main__":
    main()
