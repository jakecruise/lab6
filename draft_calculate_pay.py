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


calculate_pay(4, 10)
