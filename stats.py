def get_num_words(words):
    count = words.split()
    return len(count)

def get_letter_count(book):
    letters = list(book.lower())
    letter_count = {}
    for letter in letters:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] +=1
    return letter_count

def report(book):
    dict_list = []
    for letter in book:
        dict_list.append({"char": letter, "num": book[letter] })
    # sorted_book = sorted(book, key=lambda letter: letter[2])
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(list):
    return list["num"]