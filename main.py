from stats import count_words

def main():
    # text = get_book_text("./books/frankenstein.txt")
    number_of_words = count_words("./books/frankenstein.txt")
    print(number_of_words, "words found in the document")
    
main()