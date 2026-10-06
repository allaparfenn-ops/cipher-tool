"""Небольшой мост: QML передаёт ввод, Python возвращает результат."""

from PySide6.QtCore import QObject, Slot

from ciphers import ENGLISH, RUSSIAN, caesar


class Backend(QObject):
    # Slot делает метод доступным из QML. QVariantMap превращает
    # Python-словарь в объект, у которого QML может читать поля.
    @Slot(str, int, str, bool, result="QVariantMap")
    def process_caesar(self, text, shift, language, decrypt):
        """Шифрование и расшифровка Цезаря с пояснением замен."""
        alphabet = RUSSIAN if language == "Русский" else ENGLISH
        actual_shift = -shift if decrypt else shift
        result = caesar(text, actual_shift, alphabet)

        # Показываем несколько замен, чтобы пояснение не росло
        # вместе с большим текстом. Сам текст обрабатывается целиком.
        steps = []
        for before, after in zip(text, result):
            position = alphabet.find(before.lower())
            if position != -1:
                new_position = (position + actual_shift) % len(alphabet)
                steps.append(
                    f"{before} → {after}: ({position} + ({actual_shift})) "
                    f"mod {len(alphabet)} = {new_position}"
                )
            if len(steps) == 12:
                break

        return {
            "text": result,
            "steps": "\n".join(steps) or "Введите буквы выбранного алфавита.",
        }

    @Slot(str, str, result="QVariantMap")
    def process_atbash(self, text, language):
        """Заготовка: принимает текст и язык выбранного алфавита."""
        # У Атбаша нет ключа. Шифрование и расшифровка одинаковы,
        # поэтому параметр decrypt здесь не нужен.
        # TODO: добавить atbash в ciphers.py и импортировать её выше.
        # Затем выбрать alphabet, как в process_caesar, и вызвать:
        # result = atbash(text, alphabet)
        return {
            "text": "",
            "steps": "Шифр Атбаш пока не реализован.",
        }

    @Slot(str, str, str, bool, result="QVariantMap")
    def process_vigenere(self, text, key, language, decrypt):
        """Заготовка: текст, ключевое слово, язык и режим расшифровки."""
        # key — строка, а не число, как сдвиг у Цезаря.
        # TODO: проверить, что ключ непустой и состоит из букв алфавита.
        # Добавить vigenere в ciphers.py и импортировать её выше.
        # Затем выбрать alphabet, как в process_caesar, и вызвать:
        # result = vigenere(text, key, alphabet, decrypt)
        # В обеих заготовках после реализации вернуть result в поле text
        # и пояснение работы алгоритма в поле steps.
        return {
            "text": "",
            "steps": "Шифр Виженера пока не реализован.",
        }
