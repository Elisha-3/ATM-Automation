def ATMFunctionality():
    
    User_pin = 1234
    balance= 2000
    attempts = 3 #number of attempts required
    #forloop for user login
    for attempt in range(attempts):
        Entered_pin =int(input("Enter your 4-digit pin :"))
        if Entered_pin == User_pin:
            print("Login successful")
            break
        else:
            print("Incorrect pin")
        if attempt == attempts -1:
            print("Your card has been blocked, Visit the customer care center")


    while True:
            print("\n choose an operation: ")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Menu")
            choice= int(input("Enter 1, 2, or 3: "))
    #deposit
            if choice == 1:

                    deposit_amount= float(input("Enter the amount to deposit: "))
                    balance = balance + deposit_amount
                    print("Deposit of ",deposit_amount, "successful")
                    print("Current balance is: ",balance)

            elif choice == 2:
                      withdraw_amount = float(input("How much would you like to withdraw: "))
                      if withdraw_amount > balance:
                        print("insufficient balance")
                        print("Your current balance is ", balance)
                      else:
                        balance = balance - withdraw_amount
                        print("You withdrawal of", withdraw_amount, "was successful")
                        print("Your remaining balance is ", balance)
            elif choice == 3:
                 print("Thank you choosing to bank with us")
                 break

ATMFunctionality()