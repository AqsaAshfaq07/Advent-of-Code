def calculatePointsPart2(cards):
    cards_arr = [1 for i in range(len(cards))]

    for i in range(len(cards)):
        numbers = cards[i].split(":")[1].split("|")

        winnining_numbers =  numbers[0].strip().split()
        your_numbers =  numbers[1].strip().split()

        winnining_numbers = {int(number) for number in winnining_numbers}
        your_numbers = {int(number) for number in your_numbers}

        count = 0

        for number in your_numbers:
            if number in winnining_numbers:
                count += 1

        loopLimit = min(i + count + 1, len(cards))

        for j in range(i + 1, loopLimit):
            cards_arr[j] += cards_arr[i]

    print(sum(cards_arr))


filePath = "day4_input2.txt"
with open(filePath, "r", encoding="utf-8") as file:
    data = file.read()

line = data.strip().split("\n")
calculatePointsPart2(line) # 11024379