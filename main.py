def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def count_words(analyse):
    wordlist = []
    with open(analyse) as f:
        book_text = f.read()
    wordlist = book_text.split()
    return len(wordlist) 





def main():
    # text = get_book_text("./books/frankenstein.txt")
    number_of_words = count_words("./books/frankenstein.txt")
    print(number_of_words, "words found in the document")
    
main()