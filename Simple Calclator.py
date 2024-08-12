print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Integer")
option = int(input("Choose an operation: "))

if option in [1, 2, 3, 4, 5]:
    FirstNumber = int(input("Enter first number: "))
    SecondNumber = int(input("Enter second number: "))

    if option == 1:
        Result = FirstNumber + SecondNumber
    elif option == 2:
        Result = FirstNumber - SecondNumber
    elif option == 3:
        Result = FirstNumber * SecondNumber
    elif option == 4:
        Result = FirstNumber / SecondNumber
    elif option == 5:
        Result = FirstNumber ** SecondNumber

    print("The result is {}".format(Result))

else:
    print("Invalid operation entered")

# This is what .format does
name = "Ashe"
age = 18
greeting = "Hello, {}! You are {} years old.".format(name, age)
print(greeting)
