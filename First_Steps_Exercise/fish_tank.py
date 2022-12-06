length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume = length * width * height
volume = volume / 1000
volume = volume - (volume * percent)

print(volume)
