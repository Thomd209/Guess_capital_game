from random import randint

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
             {'China': 'Beijing'}, {'Colombia': 'Bogotá'}, {'Comoros': 'Moroni'},
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
             {'Panama': 'Panama City'}, {'Papua New Guinea': 'Port Moresby'}, {'Paraguay': 'Asunción'},
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
             {'United States of America': 'Washington, D.C.'}, {'Uruguay': 'Montevideo'}, {'Uzbekistan': 'Tashkent'}, {'Vanuatu': 'Port Vila'}, {'Vatican City (Holy See)': 'Vatican City'}, {'Venezuela': 'Caracas'}, {'Vietnam': 'Hanoi'}, {'Yemen': 'Sana\'a'}, {'Zambia': 'Lusaka'}, {'Zimbabwe': 'Harare'}]

country = ''
player_points = 0
computer_points = 0
while player_points < 3 and computer_points < 3:
    guess_country = randint(0, len(countries) - 1)
    for key in countries[guess_country]:
        country = key

    print('The country:', country)
    answer = input('Input a capital of this country: ')


    def check_answer(capital):
        for value in countries[guess_country].values():
            if capital == value:
                return True
            else:
                return False


    if check_answer(answer):
        print('Right')
        player_points += 1
    else:
        print('Wrong')
        computer_points += 1

    print(f'Player: {player_points}. Computer: {computer_points}')
    del countries[guess_country]

if player_points > computer_points:
    print("You win!")
elif computer_points > player_points:
    print("You lose")
elif player_points == computer_points:
    print("Draw")
