import datetime as dt


FORMAT = '%H%M%S'
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if None in data:     
        return False
    
    return True
    
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if len(storage_data)>0:
        if list(storage_data.keys())[len(storage_data)-1]>=time:
            return False
    
    return True

    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше или равно самому большому значению ключа в словаре,
    # функция вернет False.
    # Иначе - True 


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    return sum(list(storage_data.values()))+steps

    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.
    

def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    return round(steps * STEP_M/1000, 2)
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    if len(storage_data)>0:
        hours=current_time- list(storage_data.keys())[len(storage_data)-1]
    else:
        hours=current_time.hour+current_time.minute/60
    speed=dist/(hours)

    return round((K_1 * WEIGHT+((speed**2)/HEIGHT)*K_2*WEIGHT)*hours*60, 2)
    # В уроке «Строки» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени; 
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.

def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        return 'Отличный результат! Цель достигнута'
    elif 3.9<=dist<6.5:
        return 'Неплохо! День был продуктивным.'
    elif 2.0<=dist<3.9:
        return 'Маловато, но завтра наверстаем!'
    elif dist<2.0:
        return 'Лежать тоже полезно. главное- участие, а не победа!'
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.


def show_message(pack_time,day_steps,dist,spent_calories,achievement):
    print('Время: ', pack_time)
    print('Количество шагов за сегодня: ', day_steps)
    print('Дистанция составила ', dist, 'км')
    print('Вы сожгли ', spent_calories, 'ккал')
    print(achievement)


def accept_package(data):
    """Обработать пакет данных."""

    if  check_correct_data(data) is False:
        return 'Некорректный пакет'

    # Распакуйте полученные данные.
    pack_time =  dt.datetime.strptime(data[0],'%H:%M:%S').time()

    if  check_correct_time(pack_time) is False:
        return 'Некорректное значение времени'

    day_steps =  get_step_day(data[1])
    dist =  get_distance(day_steps)
    spent_calories = get_spent_calories(dist, pack_time)
    achievement =  get_achievement(dist)
    show_message(pack_time,day_steps,dist,spent_calories,achievement)
    storage_data[pack_time]=day_steps
    return storage_data
    # Вызовите функцию show_message().
    # Добавьте новый элемент в словарь storage_data.
    # Верните словарь storage_data.


# Данные для самопроверки.Не удаляйте их.
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)