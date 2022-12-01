word = input()
reversed_word = ""
for reversing in range(len(word) - 1, -1, -1):
    reversed_word += word[reversing]
print(reversed_word)


