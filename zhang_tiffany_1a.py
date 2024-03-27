print("This program will project how much you can earn by investing money in a high-yield savings account over a 3-month period.\n")

initial_deposit = float(input("To begin, enter how much money you would like to initiallly invest (i.e. 500): "))
interest_rate = float(input("Next, enter your projected annual interest rate. For example, enter 0.05 for 5%: "))

interest = (1 + (interest_rate/12))
month_1 = (initial_deposit * interest)
month_2 = (month_1 * interest)
month_3 = (month_2 * interest)

print("\nCalculating . . .\n") # \n adds a line break
print("Month", format("Starting Balance", '<23s'), format("Interest", '<14s'), format("Ending Balance", '<11s'))
print("1    ", format(initial_deposit, '<23.2f'), format(month_1 - initial_deposit, '<14.2f'), format(month_1, '<11.2f'))
print("2    ", format(month_1, '<23.2f'), format(month_2 - month_1, '<14.2f'), format(month_2, '<11.2f'))
print("3    ", format(month_2, '<23.2f'), format(month_3 - month_2, '<14.2f'), format(month_3, '<11.2f'))

 


