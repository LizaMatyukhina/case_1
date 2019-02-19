"""
Case #1
"""

import random
from ru_local import *


def main_questions(money, grain, people):
    """Questions about buying, selling and distribution of grain."""
    quest_buy = [Q1, Q2, Q3, Q6, Q7]
    question = random.choice(quest_buy)
    print(question)
    answer = input()
    while answer.isdigit() is False:
        print(INPUT_INT_VALUE)
        answer = input()
    answer = int(answer)
    if question == Q1:
        money = money - answer * 12
    elif question == Q2:
        money -= answer * 14
    elif question == Q3:
        money -= answer * 13
    elif question == Q6:
        money -= answer * 10
    elif question == Q7:
        money -= answer * 15
    grain += answer

    quest_sell = [Q4, Q5, Q8, Q9, Q10]
    question_2 = random.choice(quest_sell)
    print(question_2)
    answer = input()
    while answer.isdigit() is False:
        print(INPUT_INT_VALUE)
        answer = input()
    answer = int(answer)
    if question == Q4:
        money += answer * 7
    elif question == Q5:
        money += answer * 5
    elif question == Q8:
        money += answer * 6
    elif question == Q9:
        money += answer * 9
    elif question == Q10:
        money += 8
    grain -= answer

    print(DISTRIBUTION_OF_GRAIN)
    answer_3 = input()
    while answer_3.isdigit() is False:
        print(INPUT_INT_VALUE)
        answer_3 = input()
    answer_3 = int(answer)
    grain -= answer_3
    if grain / people > 90:
        people *= 1.1
    elif grain / people < 40:
        people *= 0.9
    return int(money), int(grain), int(people)


def plants(ground, grain):
    """Questions about sowing of grain."""
    print(SOWING_OF_GRAIN)
    answer_2 = input()
    while answer_2.isdigit() is False:
        print(INPUT_INT_VALUE)
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


def situation(randomness, indicators, option, no_option):
    """Random-based event generation."""
    if randomness == 1:
        n = random.randint(0, 4)
        print(option[n])
        answer = input()
        if n == 0 and answer.lower() == YES:
            if random.randint(0, 1) == 1:
                print(WIN)
                indicators['ground'] += 100
            else:
                print(LOSS)
                indicators['people'] -= 40

        elif n == 1 and answer.lower() == YES:
            if random.randint(0, 1) == 1:
                print(SUCCESSFUL_ROBBERY)
                indicators['money'] += 3000
            else:
                print(FAILED_ROBBERY)
                indicators['ground'] -= 200

        elif n == 2 and answer.lower() == YES:
            if random.randint(0, 1) == 1:
                print(FOUND_TREASURE)
                indicators['money'] += 2500
            else:
                print(NOT_FOUND_TREASURE)
                indicators['people'] -= 20

        elif n == 3 and answer.lower() == YES:
            if random.randint(0, 1) == 1:
                print(INCREASE_IN_GRAIN)
                indicators['grain'] += 2500
            else:
                print(QUACKERY)
                indicators['grain'] -= 20000

        elif n == 3 and answer.lower() == YES:
            if random.randint(0, 1) == 1:
                print(SUCCESSFUL_MARRIAGE)
                indicators['ground'] += 250
            else:
                print(NOT_SUCCESSFUL_MARRIAGE)
                indicators['money'] -= 4000
        else:
            pass

    else:
        n = random.randint(0, 7)
        print(no_option[n], end=' ')
        if n == 0:
            indicators['grain'] += 1000
            print(GRAIN_PLUS)
        if n == 1:
            indicators['money'] += 800
            print(MONEY_PLUS)
        if n == 2:
            indicators['grain'] -= 14000
            print(GRAIN_MINUS)
        if n == 3:
            indicators['money'] -= 1000
            print(MONEY_MINUS)
        if n == 4:
            indicators['people'] -= 70
            print(PEOPLE_MINUS)
        if n == 5:
            indicators['ground'] += 100
            print(GROUND_PLUS)
        if n == 6:
            indicators['ground'] -= 85
            print(GROUND_MINUS)
        if n == 7:
            indicators['people'] += 150
            print(PEOPLE_PLUS)
    return indicators


def important(ind):
    """Asking the main questions, giving the events, asking about the end of game."""
    option = [WAR, ROBBERY, TREASURE_HUNT, FERTILIZER_POTION, MARRIAGE]
    no_option = [BIRTHDAY, SECRET_ROOM_WITH_GOLD, FLOOD, ROBBERY_OF_TREASURY, PLAGUE, WATER_SHREDDING, NOMAD_RAID,
                 LONGEVITY_POTION]

    indicators = ind

    print(YEAR, indicators['year'], '\n', GROUND, indicators['ground'], '\n', MONEY, indicators['money'], '\n',
          GRAIN, indicators['grain'], '\n', PEOPLE, indicators['people'], '\n', DISTEMPER, indicators['distemper'])

    indicators['money'], indicators['grain'], indicators['people'] = main_questions(indicators['money'],
                                                                                    indicators['grain'],
                                                                                    indicators['people'])
    indicators['grain'], indicators['ground'], phrase = plants(indicators['ground'], indicators['grain'])

    indicators['year'] += 1

    if indicators['grain'] / indicators['people'] < 50 or indicators['ground'] / indicators['people'] < 1:
        indicators['distemper'] += 10
    elif indicators['distemper'] > 5:
        if indicators['grain'] / indicators['people'] > 80 or indicators['ground'] / indicators['people'] > 2.5:
            indicators['distemper'] -= 10

    print(phrase)
    indicators = situation(random.randint(0, 1), indicators, option, no_option)

    ans = input(GAME_CONTINUE)
    if ans.lower() == YES:
        if indicators['distemper'] == 100 or indicators['ground'] <= 0 or indicators['money'] <= 0 or \
                indicators['grain'] <= 0 or indicators['people'] <= 0:
            print(THE_END)
            print(TOTAL_RESULTS, '\n', YEAR, indicators['year'], '\n', GROUND, indicators['ground'], '\n', MONEY,
                  indicators['money'], '\n', GRAIN, indicators['grain'], '\n', PEOPLE, indicators['people'], '\n',
                  DISTEMPER, indicators['distemper'])
        else:
            important(ind)
    else:
        print(GAME_EXIT)
        print(YEAR, indicators['year'], '\n', GROUND, indicators['ground'], '\n', MONEY, indicators['money'],
              '\n', GRAIN, indicators['grain'], '\n', PEOPLE, indicators['people'], '\n', DISTEMPER,
              indicators['distemper'])


def main():
    """The main function."""
    indicators = {'year': 1, 'money': 21000, 'people': 500, 'ground': 1000, 'grain': 43000, 'distemper': 0}
    important(indicators)


if __name__ == '__main__':
    main()
