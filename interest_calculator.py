# Collect inputs: principal, apr, years
# calculate monthly payment
# show to user

def main():
    print("This is a monthly loan payment calculator\n")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the APR: "))
    years = int(input("Input number of years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (- amount_of_months))

    print("The monthly payment for this loan is: $" + str(round(monthly_payment, 2)))

main()