#!/bin/env=python3
from glass import Glass

def menu(question, choices):
    '''реализация меню
    question - вопрос, что выбирать
    choices - контейнер с вариантами выбора
    возвращает выбранный элемент контейнера
    '''
    print(question)
    for n, c in enumerate(choices, 1):
        print(f'{n}. {c}')
    while True:
        try:
            res = int(input('Ваш выбор >> '))
            if not 1 <= res <= len(choices):
                raise ValueError(f'Choice {res} not in menu')
            return tuple(choices)[res - 1]
        except ValueError as e:
            print(f'Ошибка: {e}. Пожалуйста, попробуйте снова.')

def ask_volume(question, *, min_vol=1, max_vol=500):
    '''реализация целочисленного запроса
    question - вопрос, что вводить
    min_vol, max_vol - диапазон вводимых значений
    возвращает введенное значение
    '''
    while True:
        try:
            amount = int(input(f'{question} ({min_vol}-{max_vol}) '))
            if not min_vol <= amount <= max_vol:
                raise ValueError(f'The value should be {min_vol}-{max_vol}, not {amount}')
            return amount
        except ValueError as e:
            print(f'Ошибка: {e}. Пожалуйста, попробуйте снова.')

def drink():
    'действие "отпить" в баре'
    liquid = glass.look()
    if liquid is None:
        print('В стакане пусто')
    else:
        print(f'В стакане {liquid}.', end=' ')
        try:
            if glass.drink(ask_volume('Сколько отопьете?')):
                print('Глык...глык...глык: Хорошо пошло !')
            else:
                print('Глык...глык: Маловато будет')
        except Exception as e:
            print(f'Ошибка при попытке отпить: {e}')
    return True

def fill():
    'действие "налить" в баре'
    liquid = menu('Что будете пить?', liquids)
    try:
        glass.fill(liquid, ask_volume('Cколько налить?'))
        print('Готово!!!')
    except Exception as e:
        print(f'Ошибка при попытке налить: {e}')
    return True

def bye():
    'действие "уйти" из бара'
    print('Заходите еще')
    return False

# варианты стаканов
glasses = {
    'Мерзавчик': Glass(125),
    'Чайный': Glass(200),
    'Граненый': Glass(250),
    'Кока-кольный': Glass(330)
}

# варианты жидкостей
liquids = ('Вода с газом', 'Вода без газа',
           'Сок березовый', 'Мед липовый',
           'Керосин', 'Электролит',
           'Отвар коры дуба')

# варианты действий в баре
actions = {'Налить': fill, 'Отпить': drink, 'Свалить': bye}

######################## main ########################
if __name__ == '__main__':
    print('Добро пожаловать в бар "На халяву"')
    
    glass = glasses[menu('Выберите стакан:', glasses.keys())]
    
    in_bar = True
    while in_bar:
        in_bar = actions[menu('Выберите действие:', actions.keys())]()
    
    print('-' * 20)
