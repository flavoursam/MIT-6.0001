import math

portion_down_payment = 0.25
r = 0.04
semi_annual_raise = 0.07

def main():
    annual_salary = 150000 #int(input("Enter the starting salary:"))
    total_cost = 1000000 #int(input("Enter the cost of your dream home: "))

    current_savings = 0.0
    
    deposit = get_deposit(total_cost, portion_down_payment)
    monthly_salary = get_monthly_salary(annual_salary)

    month = 0
    while current_savings < deposit:
        current_savings += ((current_savings*r) / 12) + monthly_salary
        month += 1
    print("current_savings:",current_savings)
    

    


def get_deposit(total_cost, portion_down_payment):
    return total_cost * portion_down_payment


def get_monthly_salary(annual_salary):
    return annual_salary / 12


if __name__== "__main__":
    main()
