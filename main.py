from stats import *


def main():
    text = read_book("./books/frankenstein.txt")
    number_of_words = count_words(text)
    chars_in_text = count_all_chars(text)
    sorted_chars = dict_to_list(chars_in_text)


    #printing all those fancy statistics 

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars :
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")

    print("============= END ===============")

main()