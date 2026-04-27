'''Anuj->The Smart Bank Account (OOPS & Dunder Methods)
The Hook: Move away from simple variables and create a robust Account object that prevents you from going broke.
The Task:
Define a class BankAccount with an __init__ for balance.
Use a Dunder Method __str__ so that when you print(account), it says "Balance: $XXXX".
Implement a withdraw() method that raises a custom Exception if the withdrawal deposit_amount is greater than the balance.
Pythonic Way: Use a "match-case" statement (Python 3.10+) to handle different transaction types (Deposit, Withdraw, View).

Initial Balance
Action
Expected Result
$100
Withdraw $150
Raise InsufficientFundsError
$100
Deposit $50
print(account) shows Balance: $150
$100
Match "View"'''

class BankAccount:
    def __init__(self,account_no):
        self.__balance = 100
        self.account_no = account_no

    @property
    def account_balance(self):
        return self.__balance
    @account_balance.setter
    def account_balance(self,deposit_amount):
        if(deposit_amount>0):
            self.account_balance = deposit_amount
        else:
            print("Balance cannot be Negative !")
    
    # magic method
    def __str__(self):
        return f"Balance : ${self.__balance}"
    # we can write this magic method like this also
    # def view(self):
    #     print(f"Bank Account no.: {self.account_no} | Balance : ${self.__balance}")

    # magic method for deposit
    def __add__(self,deposit_amount):
        if deposit_amount > 0:
            self.__balance += deposit_amount
            print(f"${deposit_amount} deposited successfully!")
        else:
            print("Negative deposit_amount cannot be deposit")

    # magic method for withdraw
    def __sub__(self, withdraw_amount):
        if(withdraw_amount>self.__balance):
            print(f"Insufficient Balance!")
        else:
            self.__balance -= withdraw_amount
            print(f"${withdraw_amount} Withdrawn successfully !")
    # Simple method if we not use magic method
    # def deposit(self,deposit_amount):
    #     if deposit_amount > 0:
    #         self + deposit_amount
    #         print(f"${deposit_amount} deposited successfully!")
    #     else:
    #         print("Negative deposit_amount cannot be deposit")

    # def withdraw(self,withdraw_amount):
    #     if(withdraw_amount>self.account_balance):
    #         print(f"Insufficient Balance!")
    #     else:
    #         self - withdraw_amount
    #         print(f"${withdraw_amount} Withdrawn successfully !")


# main Bank account class usage
print("---- Welcome to XYZ Bank ----\n")
account = BankAccount(32719281)
while True:
    print("Note: -- Enter D to Deposit \nEnter W to withdraw \nEnter V to view \nEnter E to exit")
    choice = input("Enter your choice: ")
    if choice.lower() == "w":
        withdraw_amount = int(input("Enter amount to withdraw:"))
        account - withdraw_amount
    elif choice.lower() == "d":
        deposit_amount = int(input("Enter amount to deposit: "))
        account + deposit_amount
    elif choice.lower() == "v":
        print(account)
    elif choice.lower() == "e":
        print("Exiting the Bank")
        break
    else:
        print("Invalid choice, Enter the right one!")





