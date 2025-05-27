import sys
from stats import get_char_count, sort_char_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: Could not find file at {book_path}")
        sys.exit(1)

    num_words = get_word_count(text)
    char_count = get_char_count(text)
    sorted_char_list = sort_char_dict(char_count)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_char_list:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()
