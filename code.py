sentence = input("Enter a sentence: ")
print(sentence)

characterCount = 0
wordCount = 1

for character in sentence:
    characterCount = characterCount + 1
    if (character == " "):
        wordCount = wordCount + 1
print("number of characters in string:")
print(characterCount)
print(wordCount)