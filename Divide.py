import subprocess

def Divide():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result of Division:", result)

    print("Do you want to go to menu ?")
    choice = int(input(" 1 for yes - 2 for no"))
    if choice == 1:
        subprocess.run(["python", "Calcu.py"])  
    else:
        print("thank you")



# Run the function
Divide()