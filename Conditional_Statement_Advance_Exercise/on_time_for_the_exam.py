exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

total_exam_min = (exam_hour * 60) + exam_min
total_arrival_min = (arrival_hour * 60) + arrival_min

difference_time = total_exam_min - total_arrival_min

if difference_time < 0:
    print("Late")
elif difference_time > 30:
    print("Early")
else:
    print("On time")

minutes = abs(difference_time)
hours = 0

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

result = ""

if hours > 0:
    result += str(hours) + ":" + ("0" + str(minutes) if minutes < 10 else str(minutes)) + " hours"
else:
    result += str(minutes) + " minutes"

if difference_time >= 0:
    result += " before the start"
else:
    result += " after the start"

print(result)

