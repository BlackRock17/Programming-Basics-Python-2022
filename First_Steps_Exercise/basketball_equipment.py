annual_fee = int(input())

sneakers = annual_fee - annual_fee * 0.40
clothes = sneakers - sneakers * 0.20
ball = clothes / 4
accessories = ball / 5

total = annual_fee + sneakers + clothes + ball + accessories

print(total)
