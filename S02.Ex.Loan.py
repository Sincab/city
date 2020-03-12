yearly_interest = float(input("Enter yearly interest: "))
monthly_interest = yearly_interest / 1200
number_of_years = float(input("Enter number of years you want to loan for: "))
loan_amount = float(input("Enter loan amount "))
monthly_payment = loan_amount * monthly_interest / (1 - 1 / (1 + monthly_interest)**(number_of_years*12))
total_payment = monthly_payment * number_of_years * 12
print('the monthly payment is ', monthly_payment)
print('the total payment is ',total_payment)