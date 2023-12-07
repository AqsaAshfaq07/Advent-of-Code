# power in a game = number of red * green * blue cubes
# power across multiple games = individual powers added
# find the minimum set of cubes that needs to be present and calculate the power

file_path = 'day2_2.txt'

with open(file_path, 'r') as file:
    for line in file:
        game_cubes = []


        for line in file:
            _, game_data = line.split(':')
            ball_set = game_data.split(';')

            R, G, B = [], [], []

            for set_ in ball_set:
                balls = set_.split(',')

                for ball in balls:
                    if 'green' in ball:
                        G.append(int(ball.strip().split(' ')[0]))
                    if 'blue' in ball:
                        B.append(int(ball.strip().split(' ')[0]))
                    if 'red' in ball:
                        R.append(int(ball.strip().split(' ')[0]))

            game_cubes.append(max(R) * max(G) * max(B))

        total_power = 0
        for id in game_cubes:
            total_power += id

print(total_power)