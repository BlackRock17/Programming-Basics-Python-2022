first_num = int(input())
last_num = int(input())

for i in range(first_num, last_num + 1):
    for j in range(first_num, last_num + 1):
        for k in range(first_num, last_num + 1):
            for l in range(first_num, last_num + 1):

                if (i % 2 == 0 and l % 2 != 0) or (i % 2 != 0 and l % 2 == 0):
                    if i > l:
                        if (j + k) % 2 == 0:

                            print(f"{i}{j}{k}{l}", end=" ")


