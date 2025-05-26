def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"  # Relative path
    text = get_book_text(book_path)
    print(text)

main()
