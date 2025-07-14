# Addition Calculator

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def modulo(a, b):
    return a % b


def div(a, b):
    return a / b if b != 0 else "Cannot be divisible by zero!!!"


if __name__ == "__main__":
    print(add(10, 20))
    print(sub(10, 20))
    print(modulo(10, 20))
    print(div(10, 2))
