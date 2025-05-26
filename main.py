def get_book_text(path):
    with open(path) as f:
        return f.read()
    
from stats import get_word_count


def main():
    book_path = "books/frankenstein.txt"  # Relative path
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")

main()


