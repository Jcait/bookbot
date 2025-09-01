from stats import get_num_words
from stats import get_letter_count
def get_book_text(filepath):
    contents = None
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    # words = get_book_text("books/frankenstein.txt")
    # get_num_words(words)
    get_letter_count(get_book_text("books/frankenstein.txt"))

main()