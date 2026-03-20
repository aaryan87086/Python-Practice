class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def show_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully")


# -------- MAIN ATM PROGRAM -------- 

atm = ATM(1234, 10000)

print("🏧 Welcome to ATM")

entered_pin = int(input("Enter your PIN: "))

if atm.check_pin(entered_pin):

    while True:
        print("\n------ ATM MENU ------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            atm.show_balance()

        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            atm.deposit(amount)

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        
        elif choice == 4:
            print("Thank you for using ATM 🙏")
            break

        else:
            print("Invalid choice")

else:
    print("❌ Wrong PIN. Access denied.")
