import time
class calculator:


    def __init__(self): #INITIALIZING PROGRAM WITH A SWEET WELCOME
        print("Hello and Welcome this calculator made by abdullahkghanem\nI am happy that you are using my app, now enjoy!\nThe Calculator will load now..")
        time.sleep(3)
        while True:
            try:
                self.inp1 = int(input("Enter The First Number: ")) #USER INPUT
                self.operation = int(input(
                    "What operation you want to perform?\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n"))
                self.inp2 = int(input("Enter The Second Number: "))
            except ValueError: #CHECKS THAT INPUTS ARE INTEGERS ONLY
                print("ERROR: You didn't enter a number to perform calculations on")
                continue

            if self.operation == 1: #CALCULATING AREA
                print(str(self.inp1) + " + " + str(self.inp2) + " = ", self.inp1 + self.inp2)
            elif self.operation == 2:
                print(str(self.inp1) + " - " + str(self.inp2) + " = ", self.inp1 - self.inp2)
            elif self.operation == 3:
                print(str(self.inp1) + " x " + str(self.inp2) + " = ", self.inp1 * self.inp2)
            elif self.operation == 4:
                try:
                    print(str(self.inp1) + " / " + str(self.inp2) + " = ", self.inp1 / self.inp2)
                except ZeroDivisionError:
                    print("You can't divide by ZERO.")  #SUSPENDS DIVIDING BY ZERO
            elif self.operation == 5:
                print(str(self.inp1) + " Power " + str(self.inp2) + " = ", self.inp1 ** self.inp2)
            else:
                while True: #CHECKS THAT USER IS CHOOSING A RIGHT OPERATION
                    print("You did not choose a right operation..")
                    time.sleep(1)
                    self.new = int(input("Now please enter the number of operation you want.\n"))
                    if self.new == 1: #CALCULATING AGAIN
                        print(str(self.inp1) + " + " + str(self.inp2) +
                            " = ", self.inp1 + self.inp2)
                        break
                    elif self.new == 2:
                        print(str(self.inp1) + " - " + str(self.inp2) +
                            " = ", self.inp1 - self.inp2)
                        break
                    elif self.new == 3:
                        print(str(self.inp1) + " x " + str(self.inp2) +
                            " = ", self.inp1 * self.inp2)
                        break
                    elif self.new == 4:
                        print(str(self.inp1) + " / " + str(self.inp2) +
                            " = ", self.inp1 / self.inp2)
                        break
                    elif self.new == 5:
                        print(str(self.inp1) + " Power " + str(self.inp2) +
                            " = ", self.inp1 ** self.inp2)
                        break
                    else:
                        continue

            time.sleep(1)
            
            # CHECKS IF USER WANTS TO MAKE ANOTHER CALCULATION

            self.choice = str(input("Do you want to perform another calculation?\n 1.Yes\n 2.No\n"))
            if self.choice == "2" or self.choice == "No":
                print("Quitting Application..")
                time.sleep(2)
                break
            elif self.choice == "1" or self.choice == "Yes":
                continue
App = calculator() #INITIALIZING PROGRAM INSTANCE AND CALLING THE CLASS