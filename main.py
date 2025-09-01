import sys
from stats import get_num_words
from stats import get_letter_count
from stats import report



def get_book_text(filepath):
    contents = None
    with open(filepath) as f:
        contents = f.read()
    return contents

def print_report(book_path, num_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_list:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    # words = get_book_text("books/frankenstein.txt")
    # get_num_words(words)
    # get_letter_count(get_book_text("books/frankenstein.txt"))
    # report(get_letter_count(get_book_text("books/frankenstein.txt")))
    print_report(sys.argv[1], get_num_words(get_book_text(sys.argv[1])), report(get_letter_count(get_book_text(sys.argv[1]))))
main()

