def get_list_stats():
    list_of_integers_entered = list()
    while True:
        integer_input = input('Input integers to add to a list of integers (enter space to end list):')
        if integer_input.isdigit() is True:
            list_of_integers_entered.append(int(integer_input))
            continue
        elif integer_input == ' ':
            break
        else:
            continue
    even_num_in_list = [x for x in list_of_integers_entered if x % 2 == 0]
    print(list_of_integers_entered)
    print(f'Length of the list: {len(list_of_integers_entered)}')
    print(f'Number of even numbers: {len(even_num_in_list)}')
    list_of_integers_entered.sort()
    print(f'Minimum number in list: {list_of_integers_entered[0]}')
    print(f'Maximum number in list: {list_of_integers_entered[-1]}')







get_list_stats()

# x = '5'
# y = '5.5'
# z = 'hello'
#
# print(x.isdigit())
# print(y.isdigit())
# print(z.isdigit())
#
