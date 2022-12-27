
best_movie = ""
sum = 0
counter = 0

while True:
    movie = input()
    current_sum = 0

    if movie == "STOP":
        print(f"The best movie for you is {best_movie} with {sum} ASCII sum.")
        break


    for letter in movie:
        current_sum += ord(letter)

        if letter.isupper():
            current_sum -= len(movie)
        elif letter.islower():
            current_sum -= 2 * len(movie)

        if current_sum > sum:
            sum = current_sum
            best_movie = movie

    counter += 1

    if counter == 7:
        print("The limit is reached.")
        print(f"The best movie for you is {best_movie} with {sum} ASCII sum.")
        break



