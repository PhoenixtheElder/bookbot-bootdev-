from stats import count_all_chars, count_words, read_book

def main():
    text = read_book("./books/frankenstein.txt")
    number_of_words = count_words(text)
    chars_in_text = count_all_chars(text)

    print(number_of_words, "words found in the document")
    print(chars_in_text)
main()