mackerel_prc_kg = float(input())
caca_prc_kg = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

bonito_prc_kg = mackerel_prc_kg + mackerel_prc_kg * 0.60
safrid_prc_kg = caca_prc_kg + caca_prc_kg * 0.80
mussels_prc_kg = 7.50

total_bonito = bonito_kg * bonito_prc_kg
total_safrid = safrid_kg * safrid_prc_kg
total_mussels = mussels_kg * mussels_prc_kg

total_al = total_bonito + total_safrid + total_mussels

print(f"{total_al:.2f}")

