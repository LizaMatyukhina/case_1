"""
Case #1
"""

import random

# The initial status.

# Это нужно поместить в локалку будет!
# TODO
Q1 = 'Соседнее государство предлагает вам купить зерно по 12 денежных единиц за штуку. Сколько покупаете?'
Q2 = 'Один богатый на зерно человек прелагает вам купить зерно по 14 денежных единиц! Сколько будете покупать?'
Q3 = 'Известный алхимик из соседнего государства продает зерно по 13 ден. единиц? Сколько покупаем?'
Q4 = 'Проходящие мимо странники хотят купить у вас зерно по 7 ден. единиц! Сколько будете продавать? '
Q5 = 'В соседнем государстве все посевы зерна съели мыши. Князь обратился к вам с просьбой продать ему зерно по 5 денежных ' \
     'единиц. Сколько продаете?'

def main_questions(money, grain):
    # Вопросы о покупке зерна.
    quest_buy = [Q1, Q2, Q3]
    question = random.choice(quest_buy)
    print(question)
    answer = int(input())
    if question == Q1:
        money = money - answer*12
    elif question == Q2:
        money -= answer*14
    elif question == Q3:
        money -= answer*13
    grain += answer

    # Вопросы о продаже зерна.
    quest_sell = [Q4, Q5]
    question_2 = random.choice(quest_sell)
    print(question_2)
    answer = int(input())
    if question == Q4:
        money += answer * 7
    elif question == Q5:
        money += answer * 5
    grain -= answer
    return money, grain

def main():
    year = 1
    ground = 1000
    money = 21000
    grain = 43000
    people = 500
    distemper = 0
    #Вывод некрасивый, надо исправить.
    # TODO
    print('Год:', year, '\n', 'Земля:', ground, '\n', 'Деньги:', money, '\n', 'Зерно:', grain, '\n', 'Люди:', people,
          '\n', 'Смута:', distemper)

    money, grain = main_questions(money, grain)
    year += 1


    # Смута.
    if grain / people < 50 or ground / people < 1:
        distemper += 10
    elif distemper > 5:
        if grain / people > 80 or ground / people > 2.5:
            distemper -= 10

    print('Год:', year, '\n', 'Земля:', ground, '\n', 'Деньги:', money, '\n', 'Зерно:', grain, '\n', 'Люди:', people,
          '\n', 'Смута:', distemper)

if __name__ == '__main__':
    main()
