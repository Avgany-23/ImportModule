from datetime import datetime
import locale


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

print(datetime.now().strftime(f'Сессия началась в %H:%M\nДата: %B %Y\n'))
