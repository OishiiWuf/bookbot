from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_list

import sys

def get_book_text(filepath):
    with open(filepath) as book_file:
        return book_file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    sorted_list = get_sorted_list(get_num_characters(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_list)):
        if sorted_list[i]["character"].isalpha():
            print(f"{sorted_list[i]["character"]}: {sorted_list[i]["count"]}")
    print("============= END ===============")

main()