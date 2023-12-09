def extrapolate_next_value(history):
    sequences = [history]
    while not all(value == 0 for value in sequences[-1]):
        new_sequence = [sequences[-1][i+1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)]
        sequences.append(new_sequence)

    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i+1][-1])

    return sequences[0][-1]

def extrapolate_next_value_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    histories = [list(map(int, line.strip().split())) for line in lines]

    sum_extrapolated_values = sum(extrapolate_next_value(history) for history in histories)

    return sum_extrapolated_values


file_path = 'day9.txt'
sum_extrapolated_values = extrapolate_next_value_from_file(file_path)
print(sum_extrapolated_values)