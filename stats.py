def get_num_words(words):
    count = words.split()
    print(f"{len(count)} words found in the document")

def get_letter_count(book):
    letters = list(book.lower())
    letter_count = {}
    for letter in letters:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] +=1
    print(letter_count)
    return None