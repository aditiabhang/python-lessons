vowels = ['a', 'e', 'i', 'o', 'u']

word = input("enter a word: ")

found = []

for letter in vowels:
    if letter in word:
        if letter not in found:
            found.append(letter)

for vowels in found:
        print(vowels)

