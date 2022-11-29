current_input = input()
while current_input.lower() != "end":
    if current_input == "SoftUni":
        continue
    else:
        for word in range(0, len(current_input)):
            print(current_input[word]+current_input[word], end="")

    current_input = input()
