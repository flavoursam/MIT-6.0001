import math

portion_down_payment = 0.25
r = 0.04

def main():
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream home: "))
    current_savings = 0.0
    
    deposit = get_deposit(total_cost, portion_down_payment)
    monthly_salary = get_monthly_salary(annual_salary)
    monthly_portion_saved_cost = get_monthly_portion_saved_cost(monthly_salary, portion_saved)

    months = get_num_of_months(current_savings, monthly_portion_saved_cost, deposit)
    print("Number of months:", months)
    return months

def get_num_of_months(current_savings, monthly_portion_saved_cost, deposit):
    months = 0
    current_savings = 0.0
    while current_savings < deposit:
        current_savings += ((current_savings*r) / 12) + monthly_portion_saved_cost
        months += 1
    return months

def get_deposit(total_cost, portion_down_payment):
    return portion_down_payment * total_cost

def get_monthly_portion_saved_cost(monthly_salary, portion_saved):
    return monthly_salary * portion_saved

def get_monthly_salary(annual_salary):
    return annual_salary / 12


if __name__== "__main__":
    main()
