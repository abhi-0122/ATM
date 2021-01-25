# CREATED BY:- KUMAR ABHISHEK
# LAST EDITED ON :- 25 JAN. 2021
# TIME:- 12:00 Pm
# STATUS :- WORKING ON IT

##############################################

# IMPORTING MODULES




# Creating a class (Atm)
class Atm:

    # INITIALIZING THE CLASS USING __init__
    def __init__(self):
        self._code = ""
        self.__balance = 0

        self.menu()

    # DEFINING THE "MENU" METHOD
    def menu(self):
        user_input = input("""How would you like to proceed?
        1.Press '1' to  enter your pin
        2.Press '2' to deposit money
        3.Press '3' to withdraw money
        4.Press '4' to check balance
        5.Press '5' to update Pin
        6.Press '6' to exit

         """)

        # RECALLING OF METHOD AS PER THE CHOICE OF USER

        if user_input == "1":
            self.pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "6":
            print("Have a nice day!!!")
        elif user_input == "5":
            self.update_password()
        else:
            print("Choose a valid choice")

            # RETURNS THE "MENU METHOD" WHEN THE WRONG CHOICE IS CHOSEN
            self.menu()

    # RECALL THE "PIN" METHOD  AS PER THE CHOICE

    def pin(self):
        pin = input("Enter your pin: ")
        self._code = input("Re-enter your pin: ")

        if pin == self._code:
            print("Pin is successfully changed")
            self.menu()
        else:
            print("Pin does not match")

            self.menu()

    # RECALL THE "DEPOSIT" METHOD  AS PER THE CHOICE

    def deposit(self):
        pin = input("Enter Your pin: ")
        if pin == self._code:
            amount_to_deposit = int(input("Enter the amount to be deposited: "))
            self.__balance = self.__balance + amount_to_deposit
            print("Amount in your account", self.__balance)
            self.menu()
        else:
            print("Your pin does not match")
            self.menu()
    # RECALL THE "WITHDRAW" METHOD  AS PER THE CHOICE

    def withdraw(self):
        pin = input("Enter Your pin: ")
        if self._code == pin:
            amount_to_withdraw = int(input("Enter the amount to withdraw: "))
            if self.__balance >= amount_to_withdraw:
                print("Amount left=", (self.__balance - amount_to_withdraw))
                self.menu()
            else:
                print("You don't have", amount_to_withdraw)
                print("you have ", self.__balance, "in your account")
                self.menu()
        else:
            print("Pin does not match")
            self.menu()

    # RECALL THE "CHECK_BALANCE" METHOD  AS PER THE CHOICE

    def check_balance(self):
        pin = input("Enter your pin: ")
        if pin == self._code:
            print("Your balance in account is :", self.__balance)
            self.menu()
        else:
            print("You entered wrong pin")
            self.menu()

    # RECALL THE "CHECK_BALANCE" METHOD  AS PER THE CHOICE

    def update_password(self):
        last_pin = input("Enter the last pin")
        if last_pin == self._code:
            self._code = input("Enter the new pin")
            self.menu()
        else:
            print("Your last pin does not match")
            self.menu()


bank = input("Enter the name of your bank: ")
print("Welcome user, you has your account in",bank)
bank = Atm()
