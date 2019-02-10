import math

portion_down_payment = 0.25
r = 0.04

def main():
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

    current_savings = 0.0
    
    deposit = get_deposit(total_cost, portion_down_payment)
    monthly_salary = get_monthly_salary(annual_salary)

    month = 0
    raised_monthly_salary = monthly_salary
    while current_savings < deposit:
        if month == 0 or month % 6 != 0:
            current_savings += ((current_savings*r) / 12) + (raised_monthly_salary * portion_saved)
        else:
            raised_monthly_salary += (raised_monthly_salary * semi_annual_raise)
            current_savings += ((current_savings*r) / 12) + (raised_monthly_salary * portion_saved)
        print("current savings:", current_savings)
        month += 1
    print("Number of months:", month)
    return month


def get_deposit(total_cost, portion_down_payment):
    return portion_down_payment * total_cost


def get_monthly_salary(annual_salary):
    return annual_salary / 12


if __name__== "__main__":
    main()
