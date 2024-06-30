
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a/b


print("\t *** Welcome to the calculator ***")

a = input("Enter First number: ")
b = input("Enter Second Number: ")
print("What do you want to do?")
print("1 = Addition \n2 = Subtraction \n3 = Multiplication \n4 = Division")
choice = input("Enter your Choice: ")

a = float(a)
b = float(b)
choice = int(choice)


if choice == 1:
    print(add(a, b))
elif choice == 2:
    print(sub(a, b))
elif choice == 3:
    print(mul(a, b))
elif choice == 4:
    print(div(a, b))
else:
    print("Invalid Choice")






