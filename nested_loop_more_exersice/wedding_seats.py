last_sector = input()
row_sector = int(input()) - 1
seats_odd_row = int(input())
counter = 0

for i in range(65, ord(last_sector) + 1):
    row_sector += 1
    for j in range(1, row_sector + 1):
        if j % 2 == 1:
            for k in range(97, 97 + seats_odd_row):
                counter += 1
                print(f"{chr(i)}{j}{chr(k)}")
        elif j % 2 == 0:
            for l in range(97, 97 + seats_odd_row + 2):
                counter += 1
                print(f"{chr(i)}{j}{chr(l)}")
print(counter)
