


monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expenses: "))

Monthly_savings = monthly_income - monthly_expense
print("Your monthly savings are ", Monthly_savings)
Projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is:", Projected_savings)
