#Calculator

first = input("Enter First number : ")
second = input("Enter second number : ")

first = int(first)
second = int(second)

print("============= press keys for operators (+ , - , * , / , % ) =============")

operators = input("Enter operators : ")

if operators == "+":
    print(first + second)

elif operators == "-":
    print(first - second)

elif operators == "*":
    print(first * second)

elif operators == "/":
    print(first / second)


elif operators == "%":
    print(first % second)

else:
    print("invalid operators")