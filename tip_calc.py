#A tip calculator that splits the bill between X number of people with a percentage of the bill as tip.
print("welcome to Tip Calculator\n")
Bill = input("What was the total bill?\n")
Tip = input("How much tip would you like to give (10, 12 or 15)?\n")
Tip_percent= float(Tip)/100
Tip = Tip_percent * int(Bill)
print(f"Tip is ${Tip}")

#Total bill
total_bill = Tip +int(Bill)
print(f"Total bill is ${total_bill}")

persons= input ("How many persons to split the bill?\n")
Individual_amount = total_bill / int(persons)
Individual_amount=round(float(Individual_amount),2)
#Individual_amount= "{:.2f}".format(Individual_amount)
print(f"Each person should pay ${Individual_amount}")