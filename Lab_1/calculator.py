from sys import exit


def contin():
    i = 1
    while i == 1:
        cont = input('Do you want to continue? (y-Yes/n-No):')
        if cont == 'y':
            i = 0
        elif cont == 'n':
            exit(print("End"))
        else:
            print("Incorrect symbol, try again!")


def history():
    with open("History", "r") as r:
        print(r.read())
        contin()


def save(res):
    i = 0
    while i == 0:
        save = input("Do you want to save (y-Yes/n-No): ")
        if save == 'y':
            with open("History", "a", encoding='utf-8') as w:
                w.write(str(res) + "\n")
            print("Saving")
            i = 1
            contin()
        elif save == 'n':
            print("...")
            contin()
            i = 1
        else:
            print("Incorrect symbol try again")


def result(a, b, sign, c):
    if sign == 's':
        res = (str(a) + "\u221A" + str(b) + " = " + str(c))
    else:
        res = (str(a) + str(sign) + str(b) + " = " + str(c))
    print(res)
    save(res)



def calc():
    i = 1
    numbers = 1
    while i == 1:
        a = float
        b = float
        f = int
        sign = input("Sign (+, -, *, /, **, %, s - √, h - history, c - clear history): ")
        if sign in ('h', 'c'):
            if sign == 'h':
                history()
            elif sign == 'c':
                with open("History", "w") as file:
                    file.write('\n')
                    contin()
        elif sign in ('+', '-', '*', '/', '**', '%', 's'):

            while numbers == 1:
                try:
                    a = float(input("a = "))
                    b = float(input("b = "))
                    f = int(input("Input number of float: "))
                    numbers = 0
                except ValueError:
                    print("Use only numbers!")
            f = "%." + str(f) + "f"


            if sign == '+':
                c = (f % (a + b))
                result(a, b, sign, c)
            elif sign == '-':
                c = (f % (a - b))
                result(a, b, sign, c)
            elif sign == '**':
                c = (f % (a ** b))
                result(a, b, sign, c)
            elif sign == '%':
                c = (f % (a % b))
                result(a, b, sign, c)
            elif sign == '*':
                c = (f % (a * b))
                result(a, b, sign, c)
            elif sign == '/':
                if b != 0:
                    c = (f % (a / b))
                    result(a, b, sign, c)
                else:
                    print("Division by zero!")
            elif sign == 's' or '√':
                c = a ** (1 / b)
                result(a, b, sign, c)
        else:
            print("Incorrect sign!")
