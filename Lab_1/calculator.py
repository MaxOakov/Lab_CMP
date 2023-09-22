from sys import exit
c = float

def contin():
    i = input('Do you want to continue? (y-Yes/n-No):')
    if i == 'y':
        calculator()
    elif i == 'n':
        exit(print("End"))
    else:
        print("Incorrect symbol, try again!")
        contin()


def history():
    with open("History", "r") as r:
        for line in r:
            print(r.read())


def save(res):
    save = input("Do you want to save (y-Yes/n-No): ")
    if save == 'y':
        with open("History", "a", encoding='utf-8') as w:
            w.write(str(res) + "\n")
        print("Saving")
    elif save == 'n':
        print("...")
    else:
        print("Incorrect symbol try again")


def result(a, b, sign, c):
    if sign == 's':
        res = (str(a) + "\u221A" + str(b) + " = " + str(c))
    else:
        res = (str(a) + str(sign) + str(b) + " = " + str(c))
    print(res)
    save(res)

def calculator():
    sign = input("Sign (+, -, *, /, **, %, s - √, h - history, c - clear history): ")
    if sign in ('+', '-', '*', '/', '**', '%', 's', 'h', 'c'):
        if sign == 'h':
            history()
            contin()
        elif sign == 'c':
            with open("History", "w") as file:
                file.write('\n')
                contin()
        try:
            a = float(input("a = "))
            b = float(input("b = "))
        except Exception:
            print("Input number")
            calculator()

        f = "%." + input("Input number of float: ") + "f"
        if f == '_':
            f = "%.1f"

        elif sign == '+':
            c = (f % (a + b))
            result(a,b,sign,c)
        elif sign == '-':
            c = (f % (a - b))
            result(a, b, sign, c)
        elif sign == '**':
            c = (f % (a ** b))
            result(a, b, sign, c)
        elif sign == '%':
            c = (f % (a % b))
            result(a,b,sign,c)
        elif sign == '*':
            c = (f % (a * b))
            result(a,b,sign,c)
        elif sign == '/':
            if b != 0:
                c = (f % (a / b))
                result(a, b, sign, c)
            else:
                print("Division by zero!")
        elif sign == 's' or '√':
            c = a**(1/b)
            result(a, b, sign, c)
    else:
        print("Incorrect sign!")
        calculator()


calculator()
contin()
