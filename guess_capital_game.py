from random import randint, shuffle

# the list of dictionaries consist of countries and their capitals
countries = [{'Afghanistan': 'Kabul'}, {'Albania': 'Tirana'}, {'Algeria': 'Algiers'}, {'Andorra': 'Andorra la Vella'},
             {'Angola': 'Luanda'}, {'Antigua and Barbuda': 'Saint John\'s'}, {'Argentina': 'Buenos Aires'},
             {'Armenia': 'Yerevan'}, {'Australia': 'Canberra'}, {'Austria': 'Vienna'}, {'Azerbaijan': 'Baku'},
             {'Bahamas': 'Nassau'}, {'Bahrain': 'Manama'}, {'Bangladesh': 'Dhaka'}, {'Barbados': 'Bridgetown'},
             {'Belarus': 'Minsk'}, {'Belgium': 'Brussels'}, {'Belize': 'Belmopan'}, {'Benin': 'Porto-Novo'},
             {'Bhutan': 'Thimphu'}, {'Bolivia': 'La Paz'}, {'Bosnia and Herzegovina': 'Sarajevo'},
             {'Botswana': 'Gaborone'}, {'Brazil': 'Brasilia'}, {'Brunei': 'Bandar Seri Begawan'}, {'Bulgaria': 'Sofia'},
             {'Burkina Faso': 'Ouagadougou'}, {'Burundi': 'Gitega'}, {'Cabo Verde': 'Praia'},
             {'Cambodia': 'Phnom Penh'}, {'Cameroon': 'Yaounde'}, {'Canada': 'Ottawa'},
             {'Central African Republic': 'Bangui'}, {'Chad': 'N\'Djamena'}, {'Chile': 'Santiago'},
             {'China': 'Beijing'}, {'Colombia': 'Bogota'}, {'Comoros': 'Moroni'},
             {'Congo, Democratic Republic of the': 'Kinshasa'}, {'Congo, Republic of the': 'Brazzaville'},
             {'Costa Rica': 'San Jose'}, {'Cote d\'Ivoire': 'Yamoussoukro'}, {'Croatia': 'Zagreb'}, {'Cuba': 'Havana'},
             {'Cyprus': 'Nicosia'}, {'Czechia': 'Prague'}, {'Denmark': 'Copenhagen'}, {'Djibouti': 'Djibouti (city)'},
             {'Dominica': 'Roseau'}, {'Dominican Republic': 'Santo Domingo'}, {'Ecuador': 'Quito'}, {'Egypt': 'Cairo'},
             {'El Salvador': 'San Salvador'}, {'Equatorial Guinea': 'Oyala'}, {'Eritrea': 'Asmara'},
             {'Estonia': 'Tallinn'}, {'Eswatini': 'Mbabane'}, {'Ethiopia': 'Addis Ababa'}, {'Fiji': 'Suva'},
             {'Finland': 'Helsinki'}, {'France': 'Paris'}, {'Gabon': 'Libreville'}, {'Gambia': 'Banjul'},
             {'Georgia': 'Tbilisi'}, {'Germany': 'Berlin'}, {'Ghana': 'Accra'}, {'Greece': 'Athens'},
             {'Grenada': 'Saint George\'s'}, {'Guatemala': 'Guatemala City'}, {'Guinea': 'Conakry'},
             {'Guinea-Bissau': 'Bissau'}, {'Guyana': 'Georgetown'}, {'Haiti': 'Port-au-Prince'},
             {'Honduras': 'Tegucigalpa'}, {'Hungary': 'Budapest'}, {'Iceland': 'Reykjavik'}, {'India': 'New Delhi'},
             {'Indonesia': 'Jakarta'}, {'Iran': 'Tehran'}, {'Iraq': 'Baghdad'}, {'Ireland': 'Dublin'},
             {'Israel': 'Jerusalem'}, {'Italy': 'Rome'}, {'Jamaica': 'Kingston'}, {'Japan': 'Tokyo'},
             {'Jordan': 'Amman'}, {'Kazakhstan': 'Nur-Sultan'}, {'Kenya': 'Nairobi'}, {'Kiribati': 'Tarawa'},
             {'Kosovo': 'Pristina'}, {'Kuwait': 'Kuwait City'}, {'Kyrgyzstan': 'Bishkek'}, {'Laos': 'Vientiane'},
             {'Latvia': 'Riga'}, {'Lebanon': 'Beirut'}, {'Lesotho': 'Maseru'}, {'Liberia': 'Monrovia'},
             {'Libya': 'Tripoli'}, {'Liechtenstein': 'Vaduz'}, {'Lithuania': 'Vilnius'},
             {'Luxembourg': 'Luxembourg (city)'}, {'Madagascar': 'Antananarivo'}, {'Malawi': 'Lilongwe'},
             {'Malaysia': 'Kuala Lumpur'}, {'Maldives': 'Male'}, {'Mali': 'Bamako'}, {'Malta': 'Valletta'},
             {'Marshall Islands': 'Majuro'}, {'Mauritania': 'Nouakchott'}, {'Mauritius': 'Port Louis'},
             {'Mexico': 'Mexico City'}, {'Micronesia': 'Palikir'}, {'Moldova': 'Chisinau'}, {'Monaco': 'Monaco'},
             {'Mongolia': 'Ulaanbaatar'}, {'Montenegro': 'Podgorica'}, {'Morocco': 'Rabat'}, {'Mozambique': 'Maputo'},
             {'Myanmar': 'Naypyidaw'}, {'Namibia': 'Windhoek'}, {'Nauru': 'Yaren District'}, {'Nepal': 'Kathmandu'},
             {'Netherlands': 'Amsterdam'}, {'New Zealand': 'Wellington'}, {'Nicaragua': 'Managua'}, {'Niger': 'Niamey'},
             {'Nigeria': 'Abuja'}, {'North Korea': 'Pyongyang'}, {'North Macedonia': 'Skopje'}, {'Norway': 'Oslo'},
             {'Oman': 'Muscat'}, {'Pakistan': 'Islamabad'}, {'Palau': 'Ngerulmud'}, {'Palestine': 'Jerusalem (East)'},
             {'Panama': 'Panama City'}, {'Papua New Guinea': 'Port Moresby'}, {'Paraguay': 'Asuncion'},
             {'Peru': 'Lima'}, {'Philippines': 'Manila'}, {'Poland': 'Warsaw'}, {'Portugal': 'Lisbon'},
             {'Qatar': 'Doha'}, {'Romania': 'Bucharest'}, {'Russia': 'Moscow'}, {'Rwanda': 'Kigali'},
             {'Saint Kitts and Nevis': 'Basseterre'}, {'Saint Lucia': 'Castries'},
             {'Saint Vincent and the Grenadines': 'Kingstown'}, {'Samoa': 'Apia'}, {'San Marino': 'San Marino'},
             {'Sao Tome and Principe': 'São Tomé'}, {'Saudi Arabia': 'Riyadh'}, {'Senegal': 'Dakar'},
             {'Serbia': 'Belgrade'}, {'Seychelles': 'Victoria'}, {'Sierra Leone': 'Freetown'},
             {'Singapore': 'Singapore'}, {'Slovakia': 'Bratislava'}, {'Slovenia': 'Ljubljana'},
             {'Solomon Islands': 'Honiara'}, {'Somalia': 'Mogadishu'}, {'South Africa': 'Pretoria'},
             {'South Korea': 'Seoul'}, {'South Sudan': 'Juba'}, {'Spain': 'Madrid'},
             {'Sri Lanka': 'Sri Jayawardenepura Kotte'}, {'Sudan': 'Khartoum'}, {'Suriname': 'Paramaribo'},
             {'Sweden': 'Stockholm'}, {'Switzerland': 'Bern'}, {'Syria': 'Damascus'}, {'Taiwan': 'Taipei'},
             {'Tajikistan': 'Dushanbe'}, {'Tanzania': 'Dodoma'}, {'Thailand': 'Bangkok'}, {'Timor-Leste': 'Dili'},
             {'Togo': 'Lomé'}, {'Tonga': 'Nukuʻalofa'}, {'Trinidad and Tobago': 'Port of Spain'}, {'Tunisia': 'Tunis'},
             {'Turkey': 'Ankara'}, {'Turkmenistan': 'Ashgabat'}, {'Tuvalu': 'Funafuti'}, {'Uganda': 'Kampala'},
             {'Ukraine': 'Kyiv'}, {'United Arab Emirates': 'Abu Dhabi'}, {'United Kingdom': 'London'},
             {'United States of America': 'Washington, D.C.'}, {'Uruguay': 'Montevideo'}, {'Uzbekistan': 'Tashkent'},
             {'Vanuatu': 'Port Vila'}, {'Vatican City (Holy See)': 'Vatican City'}, {'Venezuela': 'Caracas'},
             {'Vietnam': 'Hanoi'}, {'Yemen': 'Sana\'a'}, {'Zambia': 'Lusaka'}, {'Zimbabwe': 'Harare'}]

right_country = 0  # The country whose capital is the right answer
first_wrong_country = 0  # The country whose capital is the wrong answer
second_wrong_country = 0  # The country whose capital is the wrong answer
third_wrong_country = 0  # The country whose capital is the wrong answer
random_country = ''  # The country whose capital is the right answer and that will be show in the terminal
right_capital = ''  # The capital that is the right answer
first_wrong_capital = ''  # The country whose capital is the wrong answer
second_wrong_capital = ''  # The country whose capital is the wrong answer
third_wrong_capital = ''  # The country whose capital is the wrong answer
player_points = 0  # Quantity of points of the player
computer_points = 0  # Quantity of points of the computer
# The number of points up to which the game is played
while player_points < 3 and computer_points < 3:
    right_country = randint(0, len(countries) - 1)
    first_wrong_country = randint(0, len(countries) - 1)
    second_wrong_country = randint(0, len(countries) - 1)
    third_wrong_country = randint(0, len(countries) - 1)


    def get_capitals():
        # Extraction the country and capital from list item
        global first_wrong_capital, right_capital, random_country, second_wrong_capital, third_wrong_capital
        for key, value in countries[right_country].items():
            random_country = key
            right_capital = value

        # Extraction the wrong capital from list item
        for value in countries[first_wrong_country].values():
            first_wrong_capital = value

        # Extraction the wrong capital from list item
        for value in countries[second_wrong_country].values():
            second_wrong_capital = value

        # Extraction the wrong capital from list item
        for value in countries[third_wrong_country].values():
            third_wrong_capital = value

        return random_country, right_capital, first_wrong_capital, second_wrong_capital, third_wrong_capital


    random_country, right_capital, first_wrong_capital, second_wrong_capital, third_wrong_capital = get_capitals()
    # Answer options
    possible_answers = [right_capital, first_wrong_capital, second_wrong_capital, third_wrong_capital]
    # Shuffling the list randomly
    shuffle(possible_answers)
    # Output to terminal the country whose capital is the right answer
    print('The country:', random_country)
    print('Choose the right option:')
    # Output to terminal the list of mixed answers
    print(', '.join(possible_answers))
    # Inviting the user to enter the name of the capital
    player_answer = input('Input a capital of this country: ')


    # Function that checks the player answer
    def check_answer(answer):
        for capital in countries[right_country].values():
            if answer == capital:
                return True
            else:
                return False


    # Checking the user answer
    if check_answer(player_answer):
        print('Right')
        player_points += 1
    else:
        print('Wrong')
        computer_points += 1

    # Output the quantity of points of player and computer
    print(f'Player: {player_points}. Computer: {computer_points}')

    # Delete the country whose capital is the right answer
    del countries[right_country]

# Winner determination
def determinate_winner(player_scores, computer_scores):
    if player_scores > computer_scores:
        return True
    elif computer_scores > player_scores:
        return False


winner = determinate_winner(player_points, computer_points)
if winner:
    print("You win!")
elif winner is False:
    print("You lose")
