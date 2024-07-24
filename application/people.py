from tqdm import trange
from time import sleep
from application.game_sea_battle import SeaBattle
import json




def decorator_progress_bar(func: function) -> function:
    """Декоратор. Добавляет к функции прогресс бар."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in trange(20, desc="Поиск в базе"):
            sleep(0.1)
        return result
    return wrapper


@decorator_progress_bar
def person_search(name: str, password: str) -> tuple[dict, str] | bool:
    """Функция принимает имя (str) и пароль (int) пользователя.
    Если пользователь находится в persons.json, то функция выводит его данные в кортеже
    В ином случае False."""

    with open('application/persons.json', encoding='utf-8') as f:
        reader = json.load(f)['users']

        try:
            return reader[f"{name.strip('.<> ,!-/?')} {password.strip('.<>, !-/?')}"], name
        except KeyError:
            return False


def hello_person(info: tuple[dict, str]) -> str:
    """Функция выводит меню (str) пользователя."""

    return (f"Привет {info[1]}!\n"
            f"Сыграть в игру: start\n"
            f"Покинуть меню: end")


def start_search() -> None:
    """Функция для поиска пользователя в базе.
    Ничего не выводит."""
    name, password = input('Имя: '), input('Пароль: ')
    user = person_search(name, password)

    if user:
        print(hello_person(user))
        while True:
            action = input('Действие: ')

            if action == 'start':
                game = SeaBattle()
                game.start_game()
                break
            elif action == 'end':
                break
            else:
                print('Неправильное действие')
    else:
        print('Пользователь не найден')

