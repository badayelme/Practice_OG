from enum import Enum


class actions(Enum):
    Plus = 1
    Minus = 2
    Division = 3
    Multiplication = 4


def calculate(firstNumber, secondNumber, operation):
    result = 0
    match operation:
        case actions.Plus:
            result = firstNumber + secondNumber
        case actions.Minus:
            result = firstNumber - secondNumber
        case actions.Division:
            result = firstNumber / secondNumber
        case actions.Multiplication:
            result = firstNumber * secondNumber
    return firstNumber, secondNumber, operation, result


firstNumber = int(input("Enter first Number: "))
secondNumber = int(input("Enter second Number: "))
operation = actions[input("Enter operation (Plus, Minus, Division, Multiplication): ")]
print(calculate(firstNumber, secondNumber, operation))