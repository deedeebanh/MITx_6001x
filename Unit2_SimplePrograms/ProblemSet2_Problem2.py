#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 15:52:29 2021

@author: deedeebanh
"""
'''
Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310

Test Case 2:
	      balance = 4773
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 440

Test Case 3:
	      balance = 3926
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 360
'''

''' Using Iteration '''

'''
balance             = 3926
annualInterestRate  = 0.2

for lowestPayment in range(0,10000,10):
	newBalance = balance
	for i in range(12):
		newBalance = newBalance - lowestPayment
		newBalance = newBalance + newBalance * annualInterestRate / 12.0
		#print(i, newBalance)
	if newBalance < 0: break

print("Lowest Payment:", lowestPayment)
'''

''' Using Recursion '''
balance             = 4773
annualInterestRate  = 0.2

def payOfDebt(balance,annualInterestRate, lowestPayment):
    newBalance = balance

    for i in range(12):
        newBalance = newBalance - lowestPayment
        newBalance = newBalance + newBalance * annualInterestRate / 12.0

    if newBalance < 0:
        return lowestPayment
    else:
        return payOfDebt(balance,annualInterestRate, lowestPayment + 10)

print("Lowest Payment:", payOfDebt(balance,annualInterestRate, 0))
