import pyfiglet  # Task 2: connecting library
from colorama import Fore, Style


# Task 1: User input
def get_user_input():
    user_text = input("Type in your phrase (Use latin characters): ")
    return user_text


# Task 3: Choosing a font
def get_user_font():
    fonts = ['standard', '3-d', '3d-ascii', 'script']
    print("Available font styles:\n" "1. standard\n2. 3-d\n3. 3d-ascii\n4. script")
    while True:
        try:
            font = int(input("Choose a font style number (1-4):"))
            if 1 <= font <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter the correct font style number.")

    selected_font = fonts[font - 1]
    return selected_font


# Task 4: Text color
def get_user_color():
    colors = [Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX]
    print("Available text colors:\n" + Fore.LIGHTRED_EX + "1. Red\n" + Fore.LIGHTBLUE_EX + "2. Blue\n" +
          Fore.LIGHTGREEN_EX + "3. Green" + Style.RESET_ALL)

    while True:
        try:
            color_choice = int(input("Choose a text color number (1-3): "))
            if 1 <= color_choice <= 3:
                break
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter the correct text color number.")

    selected_color = colors[color_choice - 1]
    return selected_color


# Task 7: Choosing a font
def get_user_scale():
    while True:
        try:
            width = int(input("Enter the width of the ASCII art: "))
            height = int(input("Enter the height of the ASCII art: "))
            if width > 0 and height > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter the number.")
    return width, height


def get_user_char():
    while True:
        custom_char = input("Do you want to choose a special character to create ASCII art? (y/n): ").strip().lower()
        if custom_char == 'y':
            char_set = input("Enter the characters you want to use for ASCII art (eg '@#*'): ")
            break
        elif custom_char == 'n':
            char_set = None
            break
        else:
            print("Enter only \"y\" or \"n\"!")
    return char_set


def generate_ascii_art(text, selected_font, selected_color, width, height, char_set):
    ascii_text = pyfiglet.figlet_format(text=text, font=selected_font)
    scaled_ascii_text = scale_art(ascii_text, width, height, char_set)
    result = selected_color + "\n" + scaled_ascii_text + "\n" + Style.RESET_ALL
    return result


def scale_art(art, width, height, char_set):
    ascii_lines = art.split('\n')
    scaled_ascii_lines = []
    char_set_length = len(char_set) if char_set else 0
    for line in ascii_lines:
        scaled_line = ""
        for char in line:
            if char == ' ':
                scaled_line += ' '
            else:
                if char_set:
                    scaled_line += char_set[hash(char) % char_set_length]
                else:
                    scaled_line += char
        scaled_ascii_lines.append(scaled_line.center(width)[:width])
    scaled_ascii_text = '\n'.join(scaled_ascii_lines[:height])
    return scaled_ascii_text


def preview_ascii_art(result, selected_color):
    while True:
        preview_enabled = input("Want to preview your ASCII art before saving? (y/n): ").strip().lower()
        if preview_enabled == 'y':
            print(selected_color + result + Style.RESET_ALL)
            break
        if preview_enabled == 'n':
            break
        else:
            print("Enter only \"y\" or \"n\"")


# Task 6: Saving to a file
def save(ascii_text):
    while True:
        save_confirmation = input("Do you want to save ASCII art to a file? (y/n): ").strip().lower()
        if save_confirmation == 'y':
            file_name = input("Enter a file name to save the ASCII art (without extension): ")
            with open(f"{file_name}.txt", "w") as file:
                file.write(ascii_text)
            print(f"ASCII art is saved in a file {file_name}.txt")
            break
        elif save_confirmation == 'n':
            print("End of program.")
            break
        else:
            print("Enter only \"y\" or \"n\"")


def main():
    text = get_user_input()
    font = get_user_font()
    selected_color = get_user_color()
    width, height = get_user_scale()
    char_set = get_user_char()
    ascii_text = generate_ascii_art(text, font, selected_color, width, height, char_set)
    preview_ascii_art(ascii_text, selected_color)
    save(ascii_text)
