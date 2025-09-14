monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expenses: "))
Monthly_savings = monthly_income - monthly_expense
Projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)
print("Your monthly savings are ", Monthly_savings)
print("Projected savings after one year, with interest, is:", Projected_savings)
