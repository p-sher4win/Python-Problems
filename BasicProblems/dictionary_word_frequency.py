# Build a program that reads a text file and counts word frequency using a dictionary.

# opens the file, reads file content, closes the file
file = open("demo.txt")
content = file.read()
file.close()

# separates out each word generating a list of words
words = content.split()

legit_words = []
word_count_mapping = {}

# removes special characters from words
for word in words:

    """word with special char, split using join,
    checks if each char in word is alphanumeric value,
    if true returns the char or else ignores that char"""

    word = ''.join(char for char in word if char.isalnum())
    if word:
        legit_words.append(word)

# adds the word and its count to an empty dictionary
for item in legit_words:
    item_count = legit_words.count(item)
    word_count_mapping[item] = item_count

# prints the value of each word by looping through the dictionary items
for key, value in word_count_mapping.items():
    print(f"{key}: {value}")
print(f"\nTotal words: {len(legit_words)}")