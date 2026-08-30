balance = 100000
rate = 0.07
year = 1

while year <= 5:
    balance = balance * (1 + rate)
    print(f"Year {year}: {balance}")
    year += 1

for i in range(5):
    print(i)