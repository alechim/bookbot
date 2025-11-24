import sys
from stats import get_num_words, get_chars_dict, sorted_list

# Reads from a file path and returns content as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    book = get_book_text(path)
    # print(book)

    print("----------- Word Count ----------")
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    dupes = get_chars_dict(book)
    # print(dupes)
    char_list = sorted_list(dupes)
    for item in char_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()