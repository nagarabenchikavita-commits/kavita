import datetime  


balance = 5000
pin = "1234"
transaction_history = []

print(" Welcome to Python ATM")


entered_pin = input("Enter your ATM PIN: ")

if entered_pin == pin:
    while True:
        
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit & Print Receipt")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f" Your current balance is: ₹{balance}")
            transaction_history.append("Checked Balance")

        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))
            balance += amount
            transaction_history.append(f"Deposited ₹{amount}")
            print(f" ₹{amount} deposited successfully!")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= balance:
                balance -= amount
                transaction_history.append(f"Withdrew ₹{amount}")
                print(f" 12{amount} withdrawn successfully!")
            else:
                print(" Insufficient balance!")

        elif choice == "4":
            
            print("\n ===== Transaction Receipt =====")
            now = datetime.datetime.now()
            print(f"Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print("Transactions:")
            for t in transaction_history:
                print(f"- {t}")
            print(f" Final Balance: ₹{balance}")
            print("Thank you for using Python ATM! ")
            print("===================================")
            break

        else:
            print(" Invalid choice! Please try again.")
else:
    print(" Incorrect PIN! Access Denied.")
