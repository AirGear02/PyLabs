import string

input_text = str(input('Your text: '))

# Deleting punctuation and splitting into words
words = input_text.translate(str.maketrans('', '', string.punctuation)).split()
for word in words:
    if words.count(word) == 1:
        input_text = input_text.replace(word, '')
print(input_text)
