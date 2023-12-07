file_path = "day4_input.txt"

# Converting to Tables
winning_cards = []
your_cards = []

with open(file_path, 'r') as file:
    for line in file:
        line = line.replace("Card ", "").split(':')[1]
        parts = line.split('|')

        winning_numbers = [int(num) for num in parts[0].strip().split()]
        your_numbers = [int(num) for num in parts[1].strip().split()]

        # Append the lists to the respective tables
        winning_cards.append(winning_numbers)
        your_cards.append(your_numbers)

# Processing
card_len = len(your_cards)
row_len = len(your_cards[0])
total_points = 0

for i in range(card_len):
    points = 1/2
    for j in range(row_len):
        curr_num = your_cards[i][j]
        if curr_num in winning_cards[i]:
            points *= 2

    if points != 1/2:
        total_points += points

print(total_points)