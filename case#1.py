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
        money = money - answer*12
    elif question == Q2:
        money -= answer*14
    elif question == Q3:
        money -= answer*13
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
        phrase = 'Вам повезло, этот год был богат на урожай, мой Король!!'
    ground -= answer_2 // 10
    return int(grain), int(ground), phrase

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

    money, grain, people = main_questions(money, grain, people)
    grain, ground, phrase = plants(ground, grain)

    year += 1

    # Смута.
    if grain / people < 50 or ground / people < 1:
        distemper += 10
    elif distemper > 5:
        if grain / people > 80 or ground / people > 2.5:
            distemper -= 10


    print('Год:', year, '\n', 'Земля:', ground, '\n', 'Деньги:', money, '\n', 'Зерно:', grain, '\n', 'Люди:', people,
          '\n', 'Смута:', distemper)
    print(phrase)

if __name__ == '__main__':
    main()
