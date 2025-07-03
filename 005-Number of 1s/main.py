def number_of_1s(number: int) -> int:
    number_of_1s: int = 0
    for i in range(1, number + 1):
        i_string = str(i)
        for j in i_string:
            if j == "1":
                number_of_1s += 1
    return (number_of_1s)


# Eval is quick but unsafe, but here who cares honestly, it's mostly for supporting powers and stuff, shouldn't let anyone run your random daily projects in the first place
number: int = int(eval(input("Enter number: ")))
print(number_of_1s(number))
# Pretty slow all things considered, but I'm too lazy to make it quicker, as long as it works honestly.
