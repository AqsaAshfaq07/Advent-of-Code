file_path = 'day2_.txt'

possible_games = 0

with open(file_path, 'r') as file:
    for line in file:
        game = line.strip()

        given_amount = {'red': 12, 'green': 13, 'blue': 14}
        counter = {'red': 0, 'green': 0, 'blue': 0}

        arr = game.split()
        for i in range(2, len(arr) - 1):
            if 'red' in arr[i + 1]:
                counter['red'] += int(arr[i])
            elif 'green' in arr[i + 1]:
                counter['green'] += int(arr[i])
            elif 'blue' in arr[i + 1]:
                counter['blue'] += int(arr[i])

        should_continue = all(i < j for i, j in zip(counter.values(), given_amount.values()))

        if should_continue:
            num = arr[1].replace(":", "")
            possible_games += int(num)

print(possible_games)
