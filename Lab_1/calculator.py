from sys import exit


def keep_on():
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
        keep_on()


def save(res):
    i = 0
    while i == 0:
        saving = input("Do you want to save (y-Yes/n-No): ")
        if saving == 'y':
            with open("History", "a", encoding='utf-8') as w:
                w.write(str(res) + "\n")
            print("Saving")
            i = 1
            keep_on()
        elif saving == 'n':
            print("...")
            i = 1
            keep_on()
        else:
            print("Incorrect symbol try again")


def result(first_number, second_number, sign, result_number):
    if sign == 's':
        res = (str(first_number) + "\u221A" + str(second_number) + " = " + str(result_number))
    else:
        res = (str(first_number) + str(sign) + str(second_number) + " = " + str(result_number))
    print(res)
    save(res)


def sign_poll():
    valid_signs = ('+', '-', '*', '/', '**', '%', 's', 'h', 'c', 'e')

    while True:
        sign = input("Sign (+, -, *, /, **, %, s - √, h - history, c - clear history, e - end of proces): ")

        if sign in valid_signs:
            break
        else:
            print("Wrong sign. Please, input correct sign.")

    if sign in ('h', 'c', 'e'):
        if sign == 'e':
            exit(print("End"))
        elif sign == 'h':
            history()
        elif sign == 'c':
            with open("History", "w") as file:
                file.write('\n')
                keep_on()
    elif sign in ('+', '-', '*', '/', '**', '%', 's'):
        numbers_poll(sign)


def numbers_poll(sign):
    i = 1
    while i == 1:
        while True:
            try:
                a = float(input("a = "))
                b = float(input("b = "))
                f = int(input("Input number of float: "))
                break
            except ValueError:
                print("Use only numbers!")
        if sign == "/" and b == 0:
            print("Division by zero!")
        else:
            i = 0

        f = "%." + str(f) + "f"

    calc(a, b, f, sign)


def calc(first_number, second_number, float_number, sign):
    if sign == '+':
        c = (float_number % (first_number + second_number))
    elif sign == '-':
        c = (float_number % (first_number - second_number))
    elif sign == '**':
        c = (float_number % (first_number ** second_number))
    elif sign == '%':
        c = (float_number % (first_number % second_number))
    elif sign == '*':
        c = (float_number % (first_number * second_number))
    elif sign == '/':
        try:
            c = (float_number % (first_number / second_number))
        except ZeroDivisionError:
            print("Division by zero!")
    elif sign == 's' or '√':
        c = first_number ** (1 / second_number)

    result(first_number, second_number, sign, c)
