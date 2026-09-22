print("Quick Screening Tool")

income = int(input("Please enter your monthly income: "))ebt_payments = int(input("Please enter your monthly debt payments: "))

def dti(monthly_income, monthly_debt):
    ratio = debt / income
    return ratio

result = dti(monthly_income, monthly_debt_payments)

if result < 0.40:
    print(f"Approved. DTI: {result * 100}%")
else:
    print(f"Rejected. DTI: {result * 100}%")