import math
#user choice is the loop control bool variable set to true to keep looping until the user selects a valid input
user_choice = True

while user_choice == True:
    #providing the options for the user to select
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")
    #making sure that the way the user capitalises their selection does not affect how the program works using the lower() method
    user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()

    #selecting the investment option
    if user_input == "investment":
        #storing the info provided by the user in easy to understand variable names as floats
        deposit = float(input("Please enter your deposit ammount in pounds.\n"))
        interest_rate = float(input("Please enter your interest rate as a number.\n"))
        years = float(input("Please enter the number of years.\n"))

        #while loop is added to prevent the code from return to the previous block if incorrect input is provided
        while user_choice == True:
            #making sure that the way the user capitalises their selection does not affect how the program works using the lower() method
            interest = input("Please enter either simple or compound interest\n").lower()
            
            #selecting the simple interest option
            if interest == "simple":
                #calculating the answer as float
                total_amount_float = deposit * (1 + (interest_rate/100) * years)
                #limiting the float to two decimal points
                total_amount = round(total_amount_float, 2)        
                print(f"Your total amount after {years} is £{total_amount}")
                #exiting the while loop
                user_choice = False
                
            #selecting the compound interest option
            elif interest == "compound":
                #calculating the answer as float
                total_amount_float = deposit * math.pow(1 + (interest_rate/100), years)
                #limiting the float to two decimal points 
                total_amount = round(total_amount_float, 2)                
                print(f"Your total amount after {years} is £{total_amount}")
                #exiting the while loop
                user_choice = False
            else:
                print("Please enter either simple or compound.")

    #selecting the bond option
    elif user_input == "bond":
        #storing the info provided by the user in easy to understand variable names as floats
        house_value = float(input("Please enter the value of the house.\n"))
        house_interest_rate = float(input("Please enter your interest rate.\n"))        
        no_of_months = int(input("Please enter the number of months over which the bond will be repaid.\n"))
        #calculating the answer as float 
        monthly_repayment_float = (house_interest_rate/1200 * house_value) / \
        (1 - (1 + house_interest_rate/1200) ** ((-1) * no_of_months))
        #limiting the float to two decimal points
        monthly_repayment = round(monthly_repayment_float, 2)
        print(f"Your monthly repayment is £{monthly_repayment}")
        #exiting the while loop
        user_choice = False
    else:
        print("\nPlease selected either investment or bond.\n")
      