# use import math as we will be using math formulas later on in the code
import math

# I defined 'investment_a' as investiment and its definition and 'bond_a equal as bond and it definition
investment_a = "investment\t - to calculate the amount of interest you'll earn on interest "
bond_a = "bond\t\t - to calculate the amount you'll have to pay on a home loan "

# ask the user to input 'investment' or 'bond' and use 'investment_a and bond_a to shorten the code for the first output
# use .lower()  for the code to use 'investment' or 'bond' from the user selection
user = input(f" Choose either 'investment' or 'bond' from the menu below to proceed:\n{investment_a}\n{bond_a}\n").lower()

# if the user does not enter 'bond' or 'investment' ask them to try again
if (user) != "bond" and (user) != "investment":
    print(" You have not entered correctly please try again! ")
    user = input(f" Choose either 'investment' or 'bond' from the menu below to proceed:\n{investment_a}\n{bond_a}\n").lower()

# if the user enter 'investment' ask the user for 'P', 'R', calculate 'r' from 'R' and 't'
if user == "investment":
    P = float(input(" Please enter the amount of money you are depositing in rands: "))
    R = float(input(" Please enter the interest rate as a percentage, enter the number without the % "))
    r = R/100
    t = float(input(" Please enter the number of years you plan on investing for "))
# ask user to choose between simple or compound interest and save as interest
    interest = input(" Choose whether you want 'simple' or 'compound' interest ").lower()
# If useer does not enter 'simple' or 'compound' ask them to try again
    if (interest) != "simple" and (interest) != "compound":
        print(" You have not entered correctly please try again! ")
        interest = input(" Choose whether you want 'simple' or 'compound' interest ").lower()
# if user selects simple use formula to calculate the totla amount and print it
    if interest == "simple":
        A = P*(1 + r * t)
        print(A)
# if user selects compound use formula to calculate the total amount and print it
    if interest == "compound":
        A = P * math.pow((1 + r),t)
        print(A)
    
# If the user enters 'bond'  ask user for P, R save it as decimal I, calculate i monthly interest rate from anual interest rate I and n 
if user == "bond":
    P = float(input(" Please enter the present value of your house in rands: "))
    R = float(input(" Please enter the interest rate, the amount only: "))
    I = R/100
    i = I/12
    n = float(input(" Please enter number of months to repay the bond: "))
# Use formula to calculate the amount the user pays each month x and then print X
    x = (i * P)/(1 - (1 + i) ** (-n))
    print(x)           
