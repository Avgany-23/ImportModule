import json
import re


def correct_register_info(name: str, password: int) -> bool:
    """Проверка корректности имя и пароля пользователя."""
    if re.findall(r'[a-zA-Z]{2,15}', name) and re.findall(r'\d{4,30}', password):
        return True
    return False


def person_register(name: str, password: int, country: str =None, salary: int =None) -> bool:
    """Регистрация пользователя."""

    if not correct_register_info(name, password):
        return False

    with open('application/persons.json', encoding='utf-8') as f:
        reader = json.load(f)
    with open('application/persons.json', 'w', encoding='utf-8') as f:
        reader["users"][f"{name} {password}"] = {'salary': salary, 'country': country, 'experience': 0}
        json.dump(reader, f, indent=5)

    return True


def start_register() -> None:
    """Функция ничего не выводит. Регистрирует пользователя."""

    print('Введите данные')

    while True:
        name = input('Имя (на английском одно слово): ')
        password = input('Пароль (только цифры от 4 до 30): ')

        if person_register(name, password):
            print('Вы успешно зарегистрировались !\n'
                  'Войдите в свою учетную запись')
            break
        else:
            print('Неверно введены данные. Попробуйте ещё раз.')