'''
$5,000 with 18% annual interest rate and 2% minimum monthly payment rate
if pay only the minimum monthly payment for a year, what is the remaining balance

ub0 = b0 - p0
b1 = ub0 + r/12.0*ub0
ub1 = b1 - p1
b2 = ub1 + r/12.0*ub1

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

'''
'''
def CreditCardDebt(balance, annualInterestRate, monthlyPaymentRate):
    i = 0
    while i < 12:
        unpaidBalance = balance - balance * monthlyPaymentRate
        balance = unpaidBalance + annualInterestRate/12.0*unpaidBalance    
        i = i + 1
        return ("Remaining balance:", round(balance,2))

print(CreditCardDebt(42, 0.2, 0.04))
'''

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

i = 0
while i < 12:
    unpaidBalance = balance - balance * monthlyPaymentRate
    balance = unpaidBalance + annualInterestRate/12.0*unpaidBalance    
    i = i + 1
print("Remaining balance:", round(balance,2))