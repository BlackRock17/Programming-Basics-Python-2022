bitcoin = int(input())
yuan = float(input())
commission = float(input()) / 100

btc_euro = ((bitcoin * 1168) / 1.95)
yuan_euro = yuan * 0.15 * 1.76 / 1.95

total = (btc_euro + yuan_euro)

euro = total - (total * commission)

print(f"{euro:.2f}")





