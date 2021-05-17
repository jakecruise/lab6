# Phoenix Lai and Jake Cruise

# START HERE AND PASTE INTO YOUR LAB IN YOUR IDE
countries_and_capitals = (['Afghanistan', 'Kabul'], ['Albania', 'Tirana (Tirane)'], ['Algeria', 'Algiers'],
                          ['Andorra', 'Andorra la Vella'], ['Angola', 'Luanda'],
                          ['Antigua and Barbuda', "Saint John's"], ['Argentina', 'Buenos Aires'],
                          ['Armenia', 'Yerevan'], ['Australia', 'Canberra'], ['Austria', 'Vienna'],
                          ['Azerbaijan', 'Baku'], ['Bahamas', 'Nassau'], ['Bahrain', 'Manama'],
                          ['Bangladesh', 'Dhaka'], ['Barbados', 'Bridgetown'], ['Belarus', 'Minsk'],
                          ['Belgium', 'Brussels'], ['Belize', 'Belmopan'], ['Benin', 'Porto Novo'],
                          ['Bhutan', 'Thimphu'], ['Bolivia', 'Sucre'], ['Bosnia and Herzegovina', 'Sarajevo'],
                          ['Botswana', 'Gaborone'], ['Brazil', 'Brasilia'], ['Brunei', 'Bandar Seri Begawan'],
                          ['Bulgaria', 'Sofia'], ['Burkina Faso', 'Ouagadougou'], ['Burundi', 'Gitega'],
                          ['Cambodia', 'Phnom Penh'], ['Cameroon', 'Yaounde'], ['Canada', 'Ottawa'],
                          ['Cape Verde', 'Praia'], ['Central African Republic', 'Bangui'], ['Chad', "N'Djamena"],
                          ['Chile', 'Santiago'], ['China', 'Beijing'], ['Colombia', 'Bogota'], ['Comoros', 'Moroni'],
                          ['Congo, Democratic Republic of the', 'Kinshasa'], ['Congo, Republic of the', 'Brazzaville'],
                          ['Costa Rica', 'San Jose'], ["Cote d'Ivoire (Ivory Coast)", 'Yamoussoukro'],
                          ['Croatia', 'Zagreb'], ['Cuba', 'Havana'], ['Cyprus', 'Nicosia'],
                          ['Czech Republic (Czechia)', 'Prague'], ['Denmark', 'Copenhagen'], ['Djibouti', 'Djibouti'],
                          ['Dominica', 'Roseau'], ['Dominican Republic', 'Santo Domingo'], ['East Timor', 'Dili'],
                          ['Ecuador', 'Quito'], ['Egypt', 'Cairo'], ['El Salvador', 'San Salvador'],
                          ['England', 'London'], ['Equatorial Guinea', 'Malabo'], ['Eritrea', 'Asmara'],
                          ['Estonia', 'Tallinn'], ['Eswatini (Swaziland)', 'Mbabana'], ['Ethiopia', 'Addis Ababa'],
                          ['Federated States of Micronesia', 'Palikir'], ['Fiji', 'Suva'], ['Finland', 'Helsinki'],
                          ['France', 'Paris'], ['Gabon', 'Libreville'], ['Gambia', 'Banjul'], ['Georgia', 'Tbilisi'],
                          ['Germany', 'Berlin'], ['Ghana', 'Accra'], ['Greece', 'Athens'],
                          ['Grenada', "Saint George's"], ['Guatemala', 'Guatemala City'], ['Guinea', 'Conakry'],
                          ['Guinea-Bissau', 'Bissau'], ['Guyana', 'Georgetown'], ['Haiti', 'Port au Prince'],
                          ['Honduras', 'Tegucigalpa'], ['Hungary', 'Budapest'], ['Iceland', 'Reykjavik'],
                          ['India', 'New Delhi'], ['Indonesia', 'Jakarta'], ['Iran', 'Tehran'], ['Iraq', 'Baghdad'],
                          ['Ireland', 'Dublin'], ['Israel', 'Jerusalem'], ['Italy', 'Rome'], ['Jamaica', 'Kingston'],
                          ['Japan', 'Tokyo'], ['Jordan', 'Amman'], ['Kazakhstan', 'Nur-Sultan'], ['Kenya', 'Nairobi'],
                          ['Kiribati', 'Tarawa Atoll'], ['Kosovo', 'Pristina'], ['Kuwait', 'Kuwait City'],
                          ['Kyrgyzstan', 'Bishkek'], ['Laos', 'Vientiane'], ['Latvia', 'Riga'], ['Lebanon', 'Beirut'],
                          ['Lesotho', 'Maseru'], ['Liberia', 'Monrovia'], ['Libya', 'Tripoli'],
                          ['Liechtenstein', 'Vaduz'], ['Lithuania', 'Vilnius'], ['Luxembourg', 'Luxembourg'],
                          ['Madagascar', 'Antananarivo'], ['Malawi', 'Lilongwe'], ['Malaysia', 'Kuala Lumpur'],
                          ['Maldives', 'Male'], ['Mali', 'Bamako'], ['Malta', 'Valletta'],
                          ['Marshall Islands', 'Majuro'], ['Mauritania', 'Nouakchott'], ['Mauritius', 'Port Louis'],
                          ['Mexico', 'Mexico City'], ['Moldova', 'Chisinau'], ['Monaco', 'Monaco'],
                          ['Mongolia', 'Ulaanbaatar'], ['Montenegro', 'Podgorica'], ['Morocco', 'Rabat'],
                          ['Mozambique', 'Maputo'], ['Myanmar (Burma)', 'Nay Pyi Taw'], ['Namibia', 'Windhoek'],
                          ['Nauru', 'No official capital'], ['Nepal', 'Kathmandu'], ['Netherlands', 'Amsterdam'],
                          ['New Zealand', 'Wellington'], ['Nicaragua', 'Managua'], ['Niger', 'Niamey'],
                          ['Nigeria', 'Abuja'], ['North Korea', 'Pyongyang'], ['North Macedonia (Macedonia)', 'Skopje'],
                          ['Northern Ireland', 'Belfast'], ['Norway', 'Oslo'], ['Oman', 'Muscat'],
                          ['Pakistan', 'Islamabad'], ['Palau', 'Melekeok'], ['Panama', 'Panama City'],
                          ['Papua New Guinea', 'Port Moresby'], ['Paraguay', 'Asuncion'], ['Peru', 'Lima'],
                          ['Philippines', 'Manila'], ['Poland', 'Warsaw'], ['Portugal', 'Lisbon'], ['Qatar', 'Doha'],
                          ['Romania', 'Bucharest'], ['Russia', 'Moscow'], ['Rwanda', 'Kigali'],
                          ['Saint Kitts and Nevis', 'Basseterre'], ['Saint Lucia', 'Castries'],
                          ['Saint Vincent and the Grenadines', 'Kingstown'], ['Samoa', 'Apia'],
                          ['San Marino', 'San Marino'], ['Sao Tome and Principe', 'Sao Tome'],
                          ['Saudi Arabia', 'Riyadh'], ['Scotland', 'Edinburgh'], ['Senegal', 'Dakar'],
                          ['Serbia', 'Belgrade'], ['Seychelles', 'Victoria'], ['Sierra Leone', 'Freetown'],
                          ['Singapore', 'Singapore'], ['Slovakia', 'Bratislava'], ['Slovenia', 'Ljubljana'],
                          ['Solomon Islands', 'Honiara'], ['Somalia', 'Mogadishu'],
                          ['South Africa', 'Pretoria, Bloemfontein, Cape Town'], ['South Korea', 'Seoul'],
                          ['South Sudan', 'Juba'], ['Spain', 'Madrid'], ['Sri Lanka', 'Colombo'], ['Sudan', 'Khartoum'],
                          ['Suriname', 'Paramaribo'], ['Sweden', 'Stockholm'], ['Switzerland', 'Bern'],
                          ['Syria', 'Damascus'], ['Taiwan', 'Taipei'], ['Tajikistan', 'Dushanbe'],
                          ['Tanzania', 'Dodoma'], ['Thailand', 'Bangkok'], ['Togo', 'Lome'], ['Tonga', "Nuku'alofa"],
                          ['Trinidad and Tobago', 'Port of Spain'], ['Tunisia', 'Tunis'], ['Turkey', 'Ankara'],
                          ['Turkmenistan', 'Ashgabat'], ['Tuvalu', 'Funafuti'], ['Uganda', 'Kampala'],
                          ['Ukraine', 'Kiev'], ['United Arab Emirates', 'Abu Dhabi'], ['United Kingdom', 'London'],
                          ['United States', 'Washington D.C.'], ['Uruguay', 'Montevideo'], ['Uzbekistan', 'Tashkent'],
                          ['Vanuatu', 'Port Vila'], ['Vatican City', 'Vatican City'], ['Venezuela', 'Caracas'],
                          ['Vietnam', 'Hanoi'], ['Wales', 'Cardiff'], ['Yemen', "Sana'a"], ['Zambia', 'Lusaka'],
                          ['Zimbabwe', 'Harare'])

countries = ('Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
             'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
             'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
             'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
             'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
             'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Cote d'Ivoire (Ivory Coast)",
             'Croatia', 'Cuba', 'Cyprus', 'Czech Republic (Czechia)', 'Denmark', 'Djibouti', 'Dominica',
             'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'England', 'Equatorial Guinea',
             'Eritrea', 'Estonia', 'Eswatini (Swaziland)', 'Ethiopia', 'Federated States of Micronesia', 'Fiji',
             'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala',
             'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia',
             'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya',
             'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
             'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali',
             'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia',
             'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
             'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia(Macedonia)',
             'Northern Ireland', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay',
             'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
             'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
             'Sao Tome and Principe', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
             'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea',
             'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
             'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
             'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
             'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Wales', 'Yemen', 'Zambia',
             'Zimbabwe')

capitals = ('Kabul', 'Tirana (Tirane)', 'Algiers', 'Andorra la Vella', 'Luanda', "Saint John's", 'Buenos Aires',
            'Yerevan', 'Canberra', 'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels',
            'Belmopan', 'Porto Novo', 'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasilia', 'Bandar Seri Begawan',
            'Sofia', 'Ouagadougou', 'Gitega', 'Phnom Penh', 'Yaounde', 'Ottawa', 'Praia', 'Bangui', "N'Djamena",
            'Santiago', 'Beijing', 'Bogota', 'Moroni', 'Kinshasa', 'Brazzaville', 'San Jose', 'Yamoussoukro', 'Zagreb',
            'Havana', 'Nicosia', 'Prague', 'Copenhagen', 'Djibouti', 'Roseau', 'Santo Domingo', 'Dili', 'Quito',
            'Cairo', 'San Salvador', 'London', 'Malabo', 'Asmara', 'Tallinn', 'Mbabana', 'Addis Ababa', 'Palikir',
            'Suva', 'Helsinki', 'Paris', 'Libreville', 'Banjul', 'Tbilisi', 'Berlin', 'Accra', 'Athens',
            "Saint George's", 'Guatemala City', 'Conakry', 'Bissau', 'Georgetown', 'Port au Prince', 'Tegucigalpa',
            'Budapest', 'Reykjavik', 'New Delhi', 'Jakarta', 'Tehran', 'Baghdad', 'Dublin', 'Jerusalem', 'Rome',
            'Kingston', 'Tokyo', 'Amman', 'Nur-Sultan', 'Nairobi', 'Tarawa Atoll', 'Pristina', 'Kuwait City', 'Bishkek',
            'Vientiane', 'Riga', 'Beirut', 'Maseru', 'Monrovia', 'Tripoli', 'Vaduz', 'Vilnius', 'Luxembourg',
            'Antananarivo', 'Lilongwe', 'Kuala Lumpur', 'Male', 'Bamako', 'Valletta', 'Majuro', 'Nouakchott',
            'Port Louis', 'Mexico City', 'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica', 'Rabat', 'Maputo',
            'Nay Pyi Taw', 'Windhoek', 'No official capital', 'Kathmandu', 'Amsterdam', 'Wellington', 'Managua',
            'Niamey', 'Abuja', 'Pyongyang', 'Skopje', 'Belfast', 'Oslo', 'Muscat', 'Islamabad', 'Melekeok',
            'Panama City', 'Port Moresby', 'Asuncion', 'Lima', 'Manila', 'Warsaw', 'Lisbon', 'Doha', 'Bucharest',
            'Moscow', 'Kigali', 'Basseterre', 'Castries', 'Kingstown', 'Apia', 'San Marino', 'Sao Tome', 'Riyadh',
            'Edinburgh', 'Dakar', 'Belgrade', 'Victoria', 'Freetown', 'Singapore', 'Bratislava', 'Ljubljana', 'Honiara',
            'Mogadishu', 'Pretoria, Bloemfontein, Cape Town', 'Seoul', 'Juba', 'Madrid', 'Colombo', 'Khartoum',
            'Paramaribo', 'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma', 'Bangkok', 'Lome',
            "Nuku'alofa", 'Port of Spain', 'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala', 'Kiev', 'Abu Dhabi',
            'London', 'Washington D.C.', 'Montevideo', 'Tashkent', 'Port Vila', 'Vatican City', 'Caracas', 'Hanoi',
            'Cardiff', "Sana'a", 'Lusaka', 'Harare')
# END HERE


def how_many_countries():
    """ Function finds the number of countries in the tuple.
    :return: Returns the number of countries.
    """
    return len(countries)


def get_name_of_longest_country():
    """ Function finds the longest country name.
    :return: returns the longest country name.
    """
    countries_list = list(countries)
    countries_list.sort(key=len)  # sort number of char from short to long
    return countries_list[-1]


def get_number_of_capitals_containing(substring):
    """ Function find the number of capitals that include the substring.
    :param substring: Any string value.
    :return: Returns the number of capitals that include the substring.
    """
    capitals_list = list(capitals)
    capitals_with_substring = [x for x in capitals_list if substring in x.lower()]
    return len(capitals_with_substring)


def get_countries_and_capitals_that_start_with_same_letter():
    """ Function finds countries and capitals that start with the same letter.
    :return: Returns a list with countries and capitals that starts with the same letter.
    """
    count_start_with_same_letter = list()

    for country_capital in countries_and_capitals:
        country = country_capital[0]
        capital = country_capital[1]
        if country[0] != capital[0]:  # compares the first letters of country and capital
            continue
        else:
            # add onto list and format string
            count_start_with_same_letter.append(f'{country} - {capital}')
    return count_start_with_same_letter


def get_capital_of(country_for_capital_to_return):
    """ Function gets the capital name of the input country.
    :param country_for_capital_to_return: Name of a country, case insensitive.
    :return: Returns the capital of the country.
    """
    chosen_country = country_for_capital_to_return.title().strip()

    for country_capital in countries_and_capitals:
        country = country_capital[0].title().strip()
        # change input and listed country to same case to compare
        if country != chosen_country:
            continue
        else:
            return country_capital[1]
    return 'No such country'


def get_list_of_countries_with_this_many_letters_in_name(num_letters):
    """ Function find countries with the same number of letters as input.
    :param num_letters: An integer value.
    :return: Returns the list of countries with the same number of letters as input.
    """
    countries_list = []
    for country_name in countries:
        # compare input number with length of country name
        if int(num_letters) == len(country_name):
            countries_list.append(country_name)
    return countries_list


def get_capitals_and_countries_that_begin_and_end_with_same_letter():
    """ Function finds countries and capitals with the same first and last letter, case insensitive.
    :return: Returns a list of countries and capitals that begin and end with the same letter.
    """
    places_same_first_last_character = list()

    for country_capital in countries_and_capitals:
        for place in country_capital:
            place = place.lower()
            first_letter = place[0]
            last_letter = place[-1]

            # if first and last character are not the same, keep checking
            if first_letter is not last_letter:
                continue
            else:
                place = place.title()
                # format as title and add onto list
                places_same_first_last_character.append(place)
    return places_same_first_last_character


def print_countries_in_reverse_alphabetical_order():
    """ Function sorts the country names in reverse alphabetical order.
    :return: Prints a list of country names in reverse alphabetical order.
    """
    countries_list = list(countries)
    # sort alphabetically and reverse the order
    countries_list = sorted(countries_list, reverse=True)
    return print(countries_list)


print(how_many_countries())
print(get_name_of_longest_country())
print(get_number_of_capitals_containing('e'))
print(get_number_of_capitals_containing('z'))
print(get_number_of_capitals_containing("'"))
print(get_number_of_capitals_containing('an'))
print(get_countries_and_capitals_that_start_with_same_letter())
print(get_capital_of('canada'))
print(get_capital_of('nEW zeALAND'))
print(get_capital_of('xyz'))
print(get_list_of_countries_with_this_many_letters_in_name(11))
print(get_list_of_countries_with_this_many_letters_in_name(15))
print(get_capitals_and_countries_that_begin_and_end_with_same_letter())
print_countries_in_reverse_alphabetical_order()
