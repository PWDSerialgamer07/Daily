def change(number: int) -> int:

    total: dict = {"total": 0, 500: 0, 100: 0, 25: 0, 10: 0, 5: 0, 1: 0}
    if number - 500 > 0:
        total[500] = number // 500
        number -= total[500] * 500
    if number - 100 > 0:
        total[100] = number // 100
        number -= total[100] * 100
    if number - 25 > 0:
        total[25] = number // 25
        number -= total[25] * 25
    if number - 10 > 0:
        total[10] = number // 10
        number -= total[10] * 10
    if number - 5 > 0:
        total[5] = number // 5
        number -= total[5] * 5
    if number - 1 > 0:
        total[1] = number // 1
        number -= total[1] * 1
    total["total"] = total[500] + total[100] + \
        total[25] + total[10] + total[5] + total[1]

    return total


print(change(468))
