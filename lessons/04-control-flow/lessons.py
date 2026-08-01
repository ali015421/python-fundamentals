balance = 5000
if balance > 1000:
    print("Sufficient funds")

income = 9000
credit_score = 200
has_collateral = True

if income > 5000 and credit_score > 700:
    print("Auto-approved")
elif income > 5000 and has_collateral:
    print("Approved with collateral")
else:
    print("Rejected")