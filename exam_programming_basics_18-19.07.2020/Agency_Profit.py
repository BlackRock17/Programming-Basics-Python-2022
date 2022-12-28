Company_name = input()
ticket_adult = int(input())
ticket_child = int(input())
net_prc = float(input())
service = float(input())

prc_adult = net_prc + service
prc_child = (net_prc * 0.3) + service

total_prc = (ticket_adult * prc_adult) + (ticket_child * prc_child)

profit = total_prc * 0.2

print(f"The profit of your agency from {Company_name} tickets is {profit:.2f} lv.")
