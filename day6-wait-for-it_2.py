lines = open('day6.txt').readlines()

total_score = 0
curr_time = int(lines[0].strip().split(':')[1].replace(" ", ""))
curr_distance = int(lines[1].strip().split(':')[1].replace(" ", ""))
for i in range(int(curr_time)):
    if i * (curr_time - i) > curr_distance:
        total_score += 1

print(total_score)