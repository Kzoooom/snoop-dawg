import random
def gross_pay():
    return int(random.randint(5000,50000)*100)
gross_pay()
def decimals():
    return round(float(random.uniform(0,1)),2)
decimals()
def tax():
    tax_rate=round(float(random.uniform(0,1)),2)
    return tax_rate
tax()
import math
import random
# def savings():
#     # hypothetical income of the employee will range from 30000 pesos to 100000 pesos per month
#     gross_pay=int(random.randint(30000,100000)*100)
#     tax_rate=round(float(random.uniform(0,1)),2)
#     # hypothetical expenses of the employee will be 30000 pesos max to avoid negative numbers
#     expenses=int(random.randint(15000,30000)*100)
#     return (gross_pay-math.floor((gross_pay*tax_rate)))-expenses
# print(savings())

# import math
# def savings(gross_pay, tax_rate, expenses):
#     return (gross_pay - (gross_pay * tax_rate)) - expenses
# print(savings(gross_pay,tax_rate,expenses))
import math
def savings(gross_pay:int, tax_rate:float,expenses:int)->int:
    after_tax_pay=math.floor(gross_pay*(1-tax_rate))
    remaining_savings=after_tax_pay-expenses
    return remaining_savings
