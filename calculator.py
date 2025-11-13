# Hello World
import subprocess

def Calc():
    print("please enter an option")
    print("1 for addition")
    print("2 for multiply")
    print("3 for Subtraction")
    print("4 for Division")
    choice = int(input("Please enter Choice Here"))

    if choice == 1:
        subprocess.run(["python", "Addition.py"]) 
    elif choice == 2:
        subprocess.run(["python", "Multiply.py"]) 
    elif choice == 3:
        subprocess.run(["python", "Subtract.py"]) 
    elif choice == 4:
        subprocess.run(["python", "Divide.py"])         
    else:
        print("no script executed")

Calc()

