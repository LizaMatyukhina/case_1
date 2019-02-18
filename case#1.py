"""
Case #1
"""

import random
from ru_local import *


# The initial status.


def main_questions(money, grain, people):
    # Вопросы о покупке зерна.
    quest_buy = [Q1, Q2, Q3, Q6, Q7]
    question = random.choice(quest_buy)
    print(question)
    answer = input()
    while answer.isdigit() == False:
        print('Введите целочисленное значение:')
        answer = input()
    answer = int(answer)
    if question == Q1:
        money = money - answer * 12
    elif question == Q2:
        money -= answer * 14
    elif question == Q3:
        money -= answer * 13
    grain += answer


    # Вопросы о продаже зерна.
    quest_sell = [Q4, Q5, Q8, Q9, Q10]
    question_2 = random.choice(quest_sell)
    print(question_2)
    answer = input()
    while answer.isdigit() == False:
        print('Введите целочисленное значение:')
        answer = input()
    answer = int(answer)
    if question == Q4:
        money += answer * 7
    elif question == Q5:
        money += answer * 5
    grain -= answer

    # Вопрос о раздаче зерна людям.
    print(DISTRIBUTION_OF_GRAIN)
    answer_3 = input()
    while answer_3.isdigit() == False:
        print('Введите целочисленное значение:')
        answer_3 = input()
    answer_3 = int(answer)
    grain -= answer_3
    if grain / people > 90:
        people *= 1.1
    elif grain / people < 40:
        people *= 0.9
    return int(money), int(grain), int(people)


def plants(ground, grain):
    # Вопросы о посеве зерна.
    print(SOWING_OF_GRAIN)
    answer_2 = input()
    while answer_2.isdigit() == False:
        print('Введите целочисленное значение:')
        answer_2 = input()
    answer_2 = int(answer_2)
    variants = [0, 1, 2]
    plant = random.choice(variants)
    phrase = ''
    if plant == 0:
        grain += answer_2 * 0.5
        phrase = NOT_HARVEST_YEAR
    elif plant == 1:
        grain += answer_2 * 1.5
    else:
        grain += answer_2 * 2
        phrase = HARVEST_YEAR
    ground -= answer_2 // 10
    return int(grain), int(ground), phrase


def situation(randomness, indicators, option, nooption):
    '''Генерация событий на основе рандома'''
    if randomness == 1:
        l = random.randint(0, 4)
        print(option[l])
        answer = input()
        if l == 0 and answer.lower() == YES:
            if random.randint(0, 1) == 1:
                print(WIN)
                indicators['ground'] += 100
            else:
                print(LOSS)
                indicators['people'] -= 40

        elif l == 1 and answer.lower() == YES:
            if random.randint(0, 1) == 1:
                print(SUCCESSFUL_ROBBERY)
                indicators['money'] += 3000
            else:
                print(FAILED_ROBBERY)
                indicators['ground'] -= 200

        elif l == 2 and answer.lower() == YES:
            if random.randint(0, 1) == 1:
                print(FOUND_TREASURE)
                indicators['money'] += 2500
            else:
                print(NOT_FOUND_TREASURE)
                indicators['people'] -= 20

        elif l == 3 and answer.lower() == YES:
            if random.randint(0, 1) == 1:
                print(INCREASE_IN_GRAIN)
                indicators['grain'] += 2500
            else:
                print(QUACKERY)
                indicators['grain'] -= 20000

        elif l == 3 and answer.lower() == YES:
            if random.randint(0, 1) == 1:
                print(SUCCESSFUL_MARRIAGE)
                indicators['ground'] += 250
            else:
                print(NOT_SUCCESSFUL_MARRIAGE)
                indicators['money'] -= 4000
        else:
            pass

    else:
        l = random.randint(0, 7)
        print(nooption[l], end=' ')
        if l == 0:
            indicators['grain'] += 1000
            print(GRAIN_PLUS)
        if l == 1:
            indicators['money'] += 800
            print(MONEY_PLUS)
        if l == 2:
            indicators['grain'] -= 14000
            print(GRAIN_MINUS)
        if l == 3:
            indicators['money'] -= 1000
            print(MONEY_MINUS)
        if l == 4:
            indicators['people'] -= 70
            print(PEOPLE_MINUS)
        if l == 5:
            indicators['ground'] += 100
            print(GROUND_PLUS)
        if l == 6:
            indicators['ground'] -= 85
            print(GROUND_MINUS)
        if l == 7:
            indicators['people'] += 150
            print(PEOPLE_PLUS)
    return (indicators)


def important(ind):
    '''Задает основные вопросы, выдает события, спрашивает об окончании программы'''

    option = [WAR, ROBBERY, TREASURE_HUNT, FERTILIZER_POTION, MARRIAGE]
    nooption = ['День рождение у короля-соседа.', 'Потайная комната с золотом.', 'Наводнение.',
                'Ограбили казну.', 'Чума.', 'Обмельчание воды.', 'Набег кочевников.',
                'Зелье для продолжительности жизни.']

    indicators = ind

    print('Год:', indicators['year'], '\n', 'Земля:', indicators['ground'], '\n', 'Деньги:', indicators['money'],
          '\n',
          'Зерно:', indicators['grain'], '\n', 'Люди:', indicators['people'], '\n', 'Смута:',
          indicators['distemper'])

    indicators['money'], indicators['grain'], indicators['people'] = main_questions(indicators['money'],
                                                                                    indicators['grain'],
                                                                                    indicators['people'])
    indicators['grain'], indicators['ground'], phrase = plants(indicators['ground'], indicators['grain'])

    indicators['year'] += 1

    # Смута.
    if indicators['grain'] / indicators['people'] < 50 or indicators['ground'] / indicators['people'] < 1:
        indicators['distemper'] += 10
    elif indicators['distemper'] > 5:
        if indicators['grain'] / indicators['people'] > 80 or indicators['ground'] / indicators['people'] > 2.5:
            indicators['distemper'] -= 10

    print(phrase)
    indicators = situation(random.randint(0, 1), indicators, option, nooption)

    ans = input(GAME_CONTINUE)
    if ans.lower() == YES:
        important(ind)
    else:
        print(GAME_EXIT)
        print('Год:', indicators['year'], '\n', 'Земля:', indicators['ground'], '\n', 'Деньги:', indicators['money'],
              '\n',
              'Зерно:', indicators['grain'], '\n', 'Люди:', indicators['people'], '\n', 'Смута:',
              indicators['distemper'])


def main():
    indicators = {'year': 1, 'money': 21000, 'people': 500, 'ground': 1000, 'grain': 43000, 'distemper': 0}
    important(indicators)


if __name__ == '__main__':
    main()
