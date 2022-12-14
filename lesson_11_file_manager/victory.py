import random


def get_date(date):
    day_list = ['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое',
                'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                'двадцать первое', 'двадцать второе', 'двадцать третье',
                'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('.')
    return (day_list[int(date_list[0]) - 1] + ' ' + month_list[int(date_list[1]) - 1] + ' ' + date_list[2] + ' года')


def play_victory():
    name_list = ['Гагарина', 'Сталина', 'Drake', 'dr.Dre', 'Андропова', 'Черчиля', 'Трумэна', 'Энштейна', 'Джобса',
                 'Ломоносова']
    people_dict = {
        'Гагарина': '09.03.1934', 'Сталина': '18.12.1878', 'Drake': '24.10.1986', 'dr.Dre': '18.02.1965',
        'Андропова': '15.06.1914', 'Черчиля': '30.11.1874', 'Трумэна': '08.05.1884', 'Энштейна': '14.03.1879',
        'Джобса': '24.02.1955', 'Ломоносова': '19.11.1711'
    }
    good_answer = 0  # правильные ответы
    bad_answer = 0  # ложные ответы
    questions = 0  # кол-во вопросов

    while True:
        choose_person = random.sample(name_list, 5)
        for i in range(len(choose_person)):
            tmp = (input(f'Введи дату рождения {choose_person[i]}: '))
            questions += 1
            if tmp == (people_dict[choose_person[i]]):
                good_answer += 1
            else:
                bad_answer += 1
                print(f'Ошибка, правильный ответ: {get_date(people_dict[choose_person[i]])} ')
        avg_good = good_answer / questions * 100
        avg_bad = bad_answer / questions * 100
        print(
            f'Правильных ответов: {good_answer}, Неправильных ответов: {bad_answer} \nПроцент верных ответов: {avg_good}, Процент неправильных ответов: {avg_bad}')
        print('Игра окончена, хотите повторить (да/нет)?:')
        ask = input()
        if ask == 'no':
            break
        else:
            continue