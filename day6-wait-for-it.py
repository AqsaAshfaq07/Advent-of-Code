total_score = 1
lines = open('day6.txt').readlines()

for i in range(len(lines[0].split(':')[1].strip().split())):
    curr_time = lines[0].split(':')[1].strip().split()[i]
    curr_distance = lines[1].split(":")[1].strip().split()[i]
    count = 0

    for i in range(int(curr_time)):
        if i * (int(curr_time) - i) > int(curr_distance):
            count += 1

    total_score *= count

print(total_score)

