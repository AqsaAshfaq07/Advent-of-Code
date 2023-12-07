file_path = 'day1_input.txt'

with open(file_path, 'r') as file:
    # Iterate over each line in the file
    result = 0
    for line in file:
        # Process each line as needed
        string = line.strip()    # "pptqkrdbeighteightsixdlsixkrlhr2"
        arr = []
        for char in string:
            arr.append(char)
        for num in arr:
            if num.isdigit():
                start_ptr = num
                break
        for num2 in arr:
            if num2.isdigit():
                end_ptr = num2

        number = int("{}{}".format(start_ptr, end_ptr))
        result += number
print(result)