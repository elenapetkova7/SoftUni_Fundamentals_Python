number_of_messages = int(input())

for numbers in range(0, number_of_messages, 1):
    current_number = int(input())
    if current_number == 88:
        print("Hello")
    elif current_number == 86:
        print("How are you?")
    elif current_number < 88:
        print("GREAT!")
    elif current_number > 88:
        print("Bye.")



