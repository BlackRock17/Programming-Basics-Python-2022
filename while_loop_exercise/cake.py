width = int(input())
length = int(input())

num_pieces = width * length

while True:
    taken_pieces = input()

    if taken_pieces == "STOP":
        print(f"{num_pieces} pieces are left.")
        break

    pieces = int(taken_pieces)
    num_pieces -= pieces

    if num_pieces <= 0:
        print(f"No more cake left! You need {abs(num_pieces)} pieces more.")
        break

