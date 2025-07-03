import string

letters_list: list = list(string.ascii_lowercase)


def sequence(number):
    letter = letters_list[number]
    if number == 0:
        return letter
    else:
        return f"{sequence(number-1)}{letter}{sequence(number-1)}"


sequence_number: int = int(input("Enter number: ")) - 1
print(sequence(int(sequence_number)))
