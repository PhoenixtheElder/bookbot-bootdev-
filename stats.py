def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def count_words(filepath):
    wordlist = []
    with open(filepath) as f:
        book_text = f.read()
    wordlist = book_text.split()
    return len(wordlist) 
