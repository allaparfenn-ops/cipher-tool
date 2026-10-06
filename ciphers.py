"""Алгоритмы шифрования. Этот файл ничего не знает об интерфейсе Qt."""

ENGLISH = "abcdefghijklmnopqrstuvwxyz"
RUSSIAN = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def caesar(text: str, shift: int, alphabet: str) -> str:
    """Сдвигает буквы выбранного алфавита, сохраняя регистр.

    Для расшифровки достаточно передать отрицательный сдвиг.
    Пробелы, цифры и символы другого алфавита остаются на месте.
    """
    result = []

    for character in text:
        # Ищем букву без учёта регистра. find вернёт -1, если её нет.
        position = alphabet.find(character.lower())
        if position == -1:
            result.append(character)
            continue

        # Остаток от деления возвращает нас к началу алфавита:
        # для английского z при сдвиге 3 превращается в c.
        new_position = (position + shift) % len(alphabet)
        new_character = alphabet[new_position]

        if character.isupper():
            new_character = new_character.upper()

        result.append(new_character)

    return "".join(result)
