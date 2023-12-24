def add (x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division (x,y):
    return x / y

print("Enter\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division")


while True:
    
    choice = int(input("Enter your choice: "))
    if choice in (1,2,3,4):
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter first number: "))
        except ValueError:
            print("invalid input.")
            continue
        
        if choice == 1:
            print("addition: ", add(x,y))

        elif choice == 2:
            print("subtraction is: ", subtract(x,y))

        elif choice == 3:
            print("multiplication is: ", multiply(x,y))

        elif choice == 4:
            print("division is: ",division(x,y))
        
        next_calculation = input("Let's do next calculation? (yes/no)")
        if next_calculation == 'no':
            break
    else:
        print("Invalid choice")
