days = int(input())
quantity_food = float(input())

total_cat = 0
total_dog = 0
biscuits = 0

for i in range(1, days + 1):
    dog_eaten = int(input())
    cat_eaten = int(input())

    total_cat += cat_eaten
    total_dog += dog_eaten

    if i % 3 == 0:
        biscuits += (dog_eaten + cat_eaten) * 0.1

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{(total_dog + total_cat) / quantity_food * 100:.2f}% of the food has been eaten.")
print(f"{total_dog / (total_dog + total_cat) * 100:.2f}% eaten from the dog.")
print(f"{total_cat / (total_dog + total_cat) * 100:.2f}% eaten from the cat.")
