"""
Word Occurrences
"""

Words_to_count = {}

input_string = input("Text: ").lower()
words = input_string.split(' ')

for word in words:
    if word in Words_to_count:
        Words_to_count[word] += 1
    else:
        Words_to_count[word] = 1

words = list(Words_to_count.keys())
words.sort()

for word in words:
    print('{:15}: {}'.format(word, Words_to_count[word]))
