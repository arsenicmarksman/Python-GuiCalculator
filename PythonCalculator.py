#Python program for calculator

#Addition
def add(x, y):
    return x + y
#Subtraction
def subtract(x, y):
    return x - y
#Multiplication
def multiply(x, y):
    return x * y
#Division
def divide(x, y):
    return x / y
print ("Select Operation -\n" \
       "1- Add\n" \
       "2- Subtract\n" \
       "3- Multiply\n" \
       "4- Divide\n")
#Input from User
select = int(input("Select Operation from 1/ 2/ 3/ 4 :"))

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

if select == 1:
    print(x, "+", y, "=", add(x, y))

elif select == 2:
    print(x, "-", y, "=",
          subtract(x, y))

elif select == 3:
    print(x, "*", y, "=", multiply(x, y))

elif select == 4:
    print(x, "/", y, "=", divide(x, y))

else:
    print("Invalid Input")