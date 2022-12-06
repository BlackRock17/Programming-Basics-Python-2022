string = input()

sum = 0

for i in range(0, len(string)):
    letter = string[i]

    if letter == "a":
        sum += 1
    elif letter == "e":
        sum += 2
    elif letter == "i":
        sum += 3
    elif letter == "o":
        sum += 4
    elif letter == "u":
        sum += 5

print(sum)
