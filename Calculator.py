import time
import math
from colorama import init
from termcolor import colored

init() #COLORING

class calculator:

    def __init__(self):  # INITIALIZING PROGRAM WITH A SWEET WELCOME
        print(colored('Welcome to this Calculator made by abdullahkghanem\nThe Calculator will load now..','yellow'))
        time.sleep(3)
        while True:
            try:
                self.inp1 = int(
                    input("Enter The First Number: "))  # USER INPUT
                self.operation = int(input(
                    "What operation you want to perform?\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n6.Square Root\n"))
                if self.operation == 1 or self.operation == 2 or self.operation == 3 or self.operation == 4 or self.operation == 5:
                    self.inp2 = int(input("Enter The Second Number: "))
                elif self.operation == 6:
                    pass
            except ValueError:  # CHECKS THAT INPUTS ARE INTEGERS ONLY
                print(colored('ERROR: You didn\'t enter a number to perform calculations on', 'red'))
                continue

            if self.operation == 1:  # CALCULATING AREA
                print(str(self.inp1) + " + " + str(self.inp2) +
                      " = ", self.inp1 + self.inp2)
            elif self.operation == 2:
                print(str(self.inp1) + " - " + str(self.inp2) +
                      " = ", self.inp1 - self.inp2)
            elif self.operation == 3:
                print(str(self.inp1) + " x " + str(self.inp2) +
                      " = ", self.inp1 * self.inp2)
            elif self.operation == 4:
                try:
                    print(str(self.inp1) + " / " + str(self.inp2) +
                          " = ", self.inp1 / self.inp2)
                except ZeroDivisionError:
                    # SUSPENDS DIVIDING BY ZERO
                    print("You can't divide by ZERO.")
            elif self.operation == 5:
                print(str(self.inp1) + " Power " +
                      str(self.inp2) + " = ", self.inp1 ** self.inp2)
            elif self.operation == 6:
                print("Square Root of " + str(self.inp1) +
                      " is ", math.sqrt(self.inp1))
            else:
                while True:  # CHECKS THAT USER IS CHOOSING A RIGHT OPERATION
                    print(colored('ERROR: You did not choose a right operation.','red'))
                    time.sleep(1)
                    self.new = int(
                        input("Now please enter the number of operation you want.\n"))
                    if self.new == 1:  # CALCULATING AGAIN
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
                    elif self.operation == 6:
                        print("Square Root of " + str(self.inp1) +
                              " is ", math.sqrt(self.inp1))
                        break
                    else:
                        continue

            time.sleep(1)

            # CHECKS IF USER WANTS TO MAKE ANOTHER CALCULATION

            self.choice = str(
                input("Do you want to perform another calculation?\n 1.Yes\n 2.No\n"))
            if self.choice == "2" or self.choice == "No":
                print(colored('Quitting Application..','yellow'))
                time.sleep(2)
                break
            elif self.choice == "1" or self.choice == "Yes":
                continue


App = calculator()  # INITIALIZING PROGRAM INSTANCE AND CALLING THE CLASS
