number1 = float(input("Enter first Number:"))
number2 = float(input("Enter second Number:"))
operator = input("Enter Operator(+,-,*,/,%):")
if operator=="+":
    print("Result=",number1+number2)
elif operator == "-":
    print("Result =", number1 - number2)

elif operator == "*":
    print("Result =", number1 * number2)

elif operator == "/":
    if num2 != 0:
        print("Result =", number1 / number2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")