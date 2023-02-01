import operator

print("1) Add")
print("2) Substract")
print("3) Multiply")
print("4) Divide")
print("5) Exit")
while True:
    x = input("Choose an operation: ")
    if x == 5:
        break
    count = int(input("How many numbers do you need to operate: "))
    operands = [input('Value {}'.format(i + 1)) for i in range(count)]
    value = 0
    if x == 1:
        operands, value = operator.add, 0
    elif x == 2:
        operands, value = operator.sub, 0
    elif x == 3:
        operands, value = operator.mul, 1
    elif x == 4:
        operands, value = operator.truediv, 1
    for operand in operands:
        value = operand(value, operand)
    print(value)
