from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_list

def get_book_text(filepath):
    with open(filepath) as book_file:
        return book_file.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    sorted_list = get_sorted_list(get_num_characters(book_text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_list)):
        if sorted_list[i]["character"].isalpha():
            print(f"{sorted_list[i]["character"]}: {sorted_list[i]["count"]}")
    print("============= END ===============")

main()