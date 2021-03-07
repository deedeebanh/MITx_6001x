'''
Bisection
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0

      Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09

	 Test Case 2:
	      balance = 999999
	      annualInterestRate = 0.18

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 90325.03
'''


balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * (1+ monthlyInterestRate)**12) / 12.0
newBalance = balance

while abs(newBalance) > 0.01:
    newBalance = balance
    payment = (lowerBound + upperBound) / 2
    for i in range(12):
        newBalance = newBalance - payment
        newBalance = newBalance + newBalance * annualInterestRate / 12.0
    if newBalance > 0 :
        lowerBound = payment
    else:
        upperBound = payment
print("Lowest Payment:", round(payment,2))
