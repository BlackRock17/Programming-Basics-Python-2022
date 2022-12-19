first_num = int(input())
second_num = int(input())
third_num = int(input())



for i in range(1, first_num + 1):
    for j in range(1, second_num + 1):
        for k in range(1, third_num + 1):

            for l in range(2, j):

                if j % l == 0:
                    break

                if i % 2 == 0 and k % 2 == 0:
                    print(f"{i} {j} {k}")
                    break






















