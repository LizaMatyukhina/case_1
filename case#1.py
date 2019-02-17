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
    answer = int(input())
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
    answer = int(input())
    if question == Q4:
        money += answer * 7
    elif question == Q5:
        money += answer * 5
    grain -= answer

    # Вопрос о раздаче зерна людям.
    print('Сколько зерна мы будем раздавть нашим подчиненным в этом году мой Король?')
    answer_3 = int(input())
    grain -= answer_3
    if grain / people > 90:
        people *= 1.1
    elif grain / people < 40:
        people *= 0.9
    return int(money), int(grain), int(people)


def plants(ground, grain):
    # Вопросы о посеве зерна.
    print('Сколько зерна будем сеять в этом году на наших землях, мой Король?')
    answer_2 = int(input())
    variants = [0, 1, 2]
    plant = random.choice(variants)
    phrase = ''
    if plant == 0:
        grain += answer_2 * 0.5
        phrase = 'Год был неурожайный, мой Господин, к сожалению, вы зря потратили время зерно и деньги:('
    elif plant == 1:
        grain += answer_2 * 1.5
    else:
        grain += answer_2 * 2
        phrase = 'Вам повезло, этот год был богат на урожай, мой Король!!!'
    ground -= answer_2 // 10
    return int(grain), int(ground), phrase


def situation(randomness, indicators, option, nooption):
    '''Генерация событий на основе рандома'''
    if randomness == 1:
        l = random.randint(0, 4)
        print(option[l])
        answer = input()
        if l == 0 and answer.lower() == 'да':
            if random.randint(0, 1) == 1:
                print('Поздравляю, ваше королевство одержало победу. +100 к земле')
                indicators['ground'] += 100
            else:
                print('К сожалению, ваше королевство проиграло. На войне погибло 40 человек')
                indicators['people'] -= 40

        elif l == 1 and answer.lower() == 'да':
            if random.randint(0, 1) == 1:
                print('Поздравляю, ограбление прошло успешно. +3000 к казне')
                indicators['money'] += 3000
            else:
                print('К сожалению, ваших людей взяди в плен и согласились обменять на 200 у.е. земли')
                indicators['ground'] -= 200

        elif l == 2 and answer.lower() == 'да':
            if random.randint(0, 1) == 1:
                print('Поздравляю, клад был найден. +2500 к казне')
                indicators['money'] += 2500
            else:
                print('К сожалению, ваши люди зааблудились. Вы потеряли 20 человек')
                indicators['people'] -= 20

        elif l == 3 and answer.lower() == 'да':
            if random.randint(0, 1) == 1:
                print('Поздравляю, вам удалось увеличить всход зерна. +6000 у.е. зерна')
                indicators['grain'] += 2500
            else:
                print('Упс. Вы связались с шарлатаном. -20000 зерна!')
                indicators['grain'] -= 20000

        elif l == 3 and answer.lower() == 'да':
            if random.randint(0, 1) == 1:
                print('Какой удачный брак! Жених подарил вам 250 у.е. земли')
                indicators['ground'] += 250
            else:
                print('Жениху очень не понравилась невеста, он требует моральную компенсацию в размере 4000'
                      'денежных единиц')
                indicators['money'] -= 4000
        else:
            pass

    else:
        l = random.randint(0, 7)
        print(nooption[l], end=' ')
        if l == 0:
            indicators['grain'] += 1000
            print('Вы получили 1000 зерна')
        if l == 1:
            indicators['money'] += 800
            print('Вы получили 800 денег')
        if l == 2:
            indicators['grain'] -= 14000
            print('Вы потеряли 14000 зерна')
        if l == 3:
            indicators['money'] -= 1000
            print('Вы потеряли 1000 денег')
        if l == 4:
            indicators['people'] -= 70
            print('Вы потеряли 70 людей')
        if l == 5:
            indicators['ground'] += 100
            print('Вы получили 100 земли')
        if l == 6:
            indicators['ground'] -= 85
            print('Вы потеряли 85 земли')
        if l == 7:
            indicators['people'] += 150
            print('Вы получили 150 человек')
    return (indicators)


def important(ind):
    '''Задает основные вопросы, выдает события, спрашивает об окончании программы'''

    option = ['Наступила война. Готовы поучаствовать?', 'Ограбление каравана. Хотите ограбить?',
              'Ваши подданные принесли вам карту с местонахождением клада. Отправить экспедицию на поиски?',
              'Один волщебник вашего королевства варит отменные зелья в качестве удобрений. Желаете попробовать?',
              'В соседнем королевстве на троне восседает завидный жених. Выдать вашу крошку замуж?']
    nooption = ['День рождение у короля-соседа.', 'Потайная комната с золотом.', 'Наводнение.',
                'Ограбили казну.', 'Чума.', 'Обмельчание воды.', 'Набег кочевников.',
                'Зелье для продолжительности жизни.']

    indicators = ind
    # Вывод некрасивый, надо исправить.
    # TODO

    indicators['money'], indicators['grain'], indicators['people'] = main_questions(indicators['money'],
                                                                                    indicators['grain'],
                                                                                    indicators['people'])
    grain, ground, phrase = plants(indicators['ground'], indicators['grain'])

    indicators['year'] += 1

    # Смута.
    if indicators['grain'] / indicators['people'] < 50 or indicators['ground'] / indicators['people'] < 1:
        indicators['distemper'] += 10
    elif indicators['distemper'] > 5:
        if indicators['grain'] / indicators['people'] > 80 or indicators['ground'] / indicators['people'] > 2.5:
            indicators['distemper'] -= 10

    print(phrase)
    indicators = situation(random.randint(0, 1), indicators, option, nooption)

    ans = input('Хотите продолжить игру? \n')
    if ans.lower() == 'да':
        important(ind)
    else:
        print('Спасибо за участие в нашей игре, ваши итоги!')
        print("Год:", indicators['year'], '\n', 'Земля:', indicators['ground'], '\n', 'Деньги:', indicators['money'],
              '\n',
              'Зерно:', indicators['grain'], '\n', 'Люди:', indicators['people'], '\n', 'Смута:',
              indicators['distemper'])


def main():
    indicators = {'year': 1, 'money': 21000, 'people': 500, 'ground': 1000, 'grain': 43000, 'distemper': 0}
    important(indicators)


if __name__ == '__main__':
    main()
