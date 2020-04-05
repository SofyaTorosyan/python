# Homework_1 
# simple calculator

input1 = float(input()) # for floating inputs
input2 = input()
input3 = float(input())
result = 0
if input2 == "/":
    if input3 == 0:    # for dividing on zero
        print("result: ", input1, " / ", input3, " = INFINITY " )
    else:
        result = input1 / input3
        print("result: ", input1, " / ", input3, " = ", result )
elif input2 == "*":
    result = input1 * input3
    print("result: ", input1, " * ", input3, " = ", result)
elif input2 == "+":
    result = input1 + input3
    print("result: ", input1, " + ", input3, " = ", result)
elif input2 == "-":
    result = input1 - input3
    print("result: ", input1, " - ", input3, " = ", result)