"""
This is a code for a simple user friendly finance program to send money
buy airtime and also check user balance.
"""
balance= 1000.00
while True: #this line ensures the code is in a perpetual loop
    print("Enter the short code *124# to check balance, send money or buy airtime")
    choice_1=input()
    try:
        if choice_1=="*124#":
            print("Menu:")
            print('1. Check balance')
            print('2. Send money')
            print('3. Buy airtime')
            print('4. Quit')
            choice_2=input('Enter your choice:')#accepts users choice from the above menu
            if choice_2 == '1':     #code for checking balance 
                print(f'Your current balance is {balance}ghs')
            elif choice_2=='2':     #code for sending money 
                try:
                    amount=float(input('Enter amount to send:'))
                    if balance<amount:
                        print('Insufficient balance, kindly top up.')
                    else :
                        balance -= amount 
                        print(f"{amount}ghs sent successfully. Current balance is {balance}")
                except ValueError:  #the block of code below ensures invalid input doesn't crash the code
                    print('Invalid input. Please enter a valid amount.')        
            elif choice_2=='3':     #code for buying airtime
                try:
                    air_amount=float(input('Enter airtime amount:'))
                    cost=air_amount/2   #since airtime costs half the actual amount
                    if air_amount>balance:
                        print('Insufficient balance, kindly top up')
                    else:
                        balance-=cost
                        print(f'Airtime amount of {air_amount} has successfully been purchased')
                        print(f'Current balance is {balance}ghs')
                except ValueError:  #the block of code below ensures invalid input doesn't crash the code
                    print('Invalid input. Please enter a valid amount.')                
            elif choice_2=='4':     #code for exiting the looped program
                print('Thank you for using our service. Goodbye!')
                break
            else:
                print("Invalid choice. Please select a valid option from the menu.")
        else:
             print('Invalid input')
    except ValueError:
        print('Invalid choice')