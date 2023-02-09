budget = float(input())
num_video_card = int(input())
num_processor = int(input())
num_ram = int(input())

prc_video = 250
prc_processor = num_video_card * prc_video * 0.35
prc_ram = num_video_card * prc_video * 0.10

total_prc = (num_video_card * prc_video) + \
            (num_processor * prc_processor) + \
            (num_ram * prc_ram)

if num_video_card > num_processor:
    total_prc = total_prc * 0.85

if budget >= total_prc:
    print(f"You have {budget - total_prc:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_prc - budget:.2f} leva more!")

