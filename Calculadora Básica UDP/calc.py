def calculator(num1, num2, op):
    num1, num2 = int(num1), int(num2)

    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2:
            return num1/num2
        else:
            return 'Operação Inválida'