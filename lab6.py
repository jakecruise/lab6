# Jake Cruise and ...


def weight_converter():
    for weight_kg in range(30, 101, 10):
        weight_lb = (weight_kg * 2.2)
        print(f'Weight in Kilos: {weight_kg:5d} is {weight_lb:6.2f} in Pounds')


def get_divisible():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    divisor = int(input('Enter divisor: '))
    divisible_by_divisor = list()
    if divisor == 0:
        print('The divisor cannot be zero')
        return
    elif first_number < second_number:
        for numbers_between_first_second in range(first_number,second_number + 1):
            if numbers_between_first_second % divisor == 0:
                divisible_by_divisor.append(numbers_between_first_second)
            else:
                continue
    elif first_number > second_number:
        for numbers_between_first_second in range(second_number + 1, first_number):
            if numbers_between_first_second % divisor == 0:
                divisible_by_divisor.append(numbers_between_first_second)
                divisible_by_divisor.sort(reverse=True)
            else:
                continue
    print(divisible_by_divisor)


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


def calculate_pay(num_employees, hourly_rate):
    all_employees_hours_and_pay = list()
    for employee in range(1, num_employees + 1):
        hours_worked = float(input(f'Enter the number of worked hours for employee {employee}:'))
        if hours_worked <= 40:
            total_pay_for_employee = hours_worked * hourly_rate
        else:
            total_pay_for_employee = (40 * hourly_rate) + ((hours_worked - 40) * hourly_rate * 1.5)
        employee_hours_worked_and_pay = [hours_worked, total_pay_for_employee]
        all_employees_hours_and_pay.append(employee_hours_worked_and_pay)
    for employee_hours_worked_and_pay in all_employees_hours_and_pay:
        print(f'The employee worked for {employee_hours_worked_and_pay[0]:.0f} hours and earned '
              f'${employee_hours_worked_and_pay[1]:.2f}')


def main():
    weight_converter()
    get_divisible()
    get_list_stats()
    calculate_pay(4, 10)


if  __name__ == "__main__":
    main()
