def sum_of_squares(number: int) -> int:
    number_string = str(number)
    sum_of_squares = 0
    for i in number_string:
        sum_of_squares += int(i)**2
    return sum_of_squares


def is_happy_number(number: int) -> bool:
    seen = set()
    while number not in seen:
        seen.add(number)
        number = sum_of_squares(number)
    return number == 1


number = int(input("Enter number: "))
print(is_happy_number(number))
