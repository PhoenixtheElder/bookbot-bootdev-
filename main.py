def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(text)
    return 0

main()