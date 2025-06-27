word:str = "microspectrophotometries"
values:list = []

for i in word:
    value:int = ord(i) - 96 # -96 because in the ascii, letters start at 97.
    values.append(value)

sum:int = sum(values)
print(sum)