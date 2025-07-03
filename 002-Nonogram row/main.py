import random  # for testing the function latter


def nonograms_row(nonogram_list: list) -> list:
    result: list = []
    k: int = 0
    for i in nonogram_list:
        if i == 1:
            k += 1
        else:
            if k != 0:
                result.append(k)
            k = 0
    if k != 0:
        result.append(k)  # append the last k
    return result


testing_list: list = []
for i in range(30):
    testing_list.append(random.randint(0, 1))
test = nonograms_row(testing_list)
print(testing_list)
print(test)
