from application.salary import calculate_salary
from application.db.people import get_employees
from dirty_main import *
import datetime


if __name__ == '__main__':
    print('Запустили основной модуль:', __name__)
    date = datetime.datetime.today()
    print('Сегодня:', date.strftime('%d-%B-%Y'))
    calculate_salary()
    get_employees()
    test()