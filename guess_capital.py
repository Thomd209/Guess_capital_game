from random import randint

countries = [{'Russia': 'Moscow'}, {'USA': 'Washington'}, {'Canada': 'Ottawa'}]
country = ''
player_points = 0
computer_points = 0
while len(countries) != 0:
    guess_country = randint(0, len(countries) - 1)
    for key in countries[guess_country]:
        country = key

    print('Страна, столицу которой Вам нужно назвать:', country)
    answer = input('Введите название столицы страны: ')

    def check_answer(capital):
        for i in countries[guess_country].values():
            if capital == i:
                return True
            else:
                return False

    if check_answer(answer):
        print('Вы выиграли')
        player_points += 1
    else:
        print('Вы проиграли')
        computer_points += 1

    print(f'Игрок: {player_points}, компьютер: {computer_points}')
    del countries[guess_country]
