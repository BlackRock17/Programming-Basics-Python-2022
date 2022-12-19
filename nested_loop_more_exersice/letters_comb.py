first_letter = ord(input())
second_letter = ord(input())
third_letter = ord(input())
counter = 0

for i in range(first_letter, second_letter + 1):
    for j in range(first_letter, second_letter + 1):
        for k in range(first_letter, second_letter + 1):

            if i == third_letter or j == third_letter or k == third_letter:
                continue

            else:
                counter += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")

print(counter)