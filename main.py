from application.people import start_search
from application.register import start_register


if __name__ == '__main__':
    # Пример для входа: Christopher - логин, 1234 - пароль
    print('Введите действие\n'
          '-> войти\n'
          '-> зарегистрироваться\n')

    while True:
        action = input('Действие: ').lower()

        if action == 'войти':
            start_search()
        elif action == 'зарегистрироваться':
            start_register()
        else:
            print('Неправильное действие')
