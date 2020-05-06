import string
import random

fw = open("staff.txt", "w")
fw.write("austino, 4567cass, austino@gmail.com, Austin Dibie\n")
fw.write("henrietta, 45cass67, henrietta@gmail.com, Henrietta Ashiedu")
fw.close()

fc = open("customerdata.txt", "w")
fc.close()

login = True
success = True
sessionStart = True
while login:
    print("Welcome to the bank of startNG")
    print()
    print("What will you like to do?")
    print()
    try:
        loginChoice = int(input("Enter 1 to log in\nEnter 2 to log out:"))

        while success:
            '''This while loop runs if user chooses to log in'''

            if loginChoice == 2:
                print("Do have a nice day")
                login = False
                success = False
            elif loginChoice == 1:
                # open file
                fr = open("staff.txt", "r")
                staffData = fr.read().splitlines()
                fr.close()

                print("Please input your username and password")
                user = input("Username:") + ","

                for i in staffData:
                    if user in i:
                        print(f"Welcome online")
                        data_to_use = i.split()
                        pwd = str(input("Password:")) + ","
                        print()
                        if pwd == data_to_use[1]:
                            while sessionStart:
                                print("Logged in. Choose your option with the corresponding number")
                                print()
                                action = int(input("1. Create account\n"
                                                   "2. Check account info\n"
                                                   "3. Logout"
                                                   ":"))
                                print()
                                if action == 3:
                                    print("Do have a nice day")
                                    login = False
                                    success = False
                                    sessionStart = False
                                elif action == 1:
                                    print("Account Creation page")
                                    accountName = input("Account name: ")
                                    openingBalance = input("Opening Balance: ")
                                    accountType = input("Account Type: ")
                                    accountEmail = input("Account Email: ")
                                    chars = string.digits
                                    accountNumber = "".join(random.choice(chars) for x in range(1, 11))
                                    fc = open('customerdata.txt', 'w')
                                    fc.write(
                                        f'{accountName} {openingBalance} {accountType} {accountEmail} {accountNumber}')
                                    fc.close()
                                    print(f"The account number is {accountNumber}")
                                elif action == 2:
                                    fr = open("customerdata.txt", "r")
                                    customerData = fr.read().splitlines()

                                    fr.close()
                                    print(customerData)
                                    print("Input Account Number")
                                    print()
                                    dataChecker = input(":")
                                    for d in customerData:
                                        if dataChecker in d:
                                            finalOutput = d.split()
                                            print(finalOutput)
                                            print(type(finalOutput))
                                            print(f"Account name: {finalOutput[0]}\n"
                                                  f"Opening balance: {finalOutput[1]}\n"
                                                  f"Account type: {finalOutput[2]}\n"
                                                  f"Account email: {finalOutput[3]}\n"
                                                  f"Account number: {finalOutput[4]}")
                                        else:
                                            print("No data")

                if pwd != data_to_use[1]:  # username not found
                    print("Wrong info Try again")
                    break
    except ValueError:
        print("Please type only a single digit")
