count_of_number = int(input())
even_numbers = True

for count in range(count_of_number):
    number = int(input())
    if number % 2 == 1:
        even_numbers = False
        print(f"{number} is odd!")
        break
    else:
        even_numbers = True

if even_numbers:
    print("All numbers are even.")
