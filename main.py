from stats import *
import sys

def main():
    
    #Eingabe des Pfades des zu analysierenden Textes
    script = sys.argv[0] #dies sollte immer "main.py" sein
    
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    #Fehlermeldung bei zu wenig Parametern (müssen 2 sein)
    else:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)

    

    
    #Festlegen der Variablen anhand des Textes
    text = read_book(filepath)
    number_of_words = count_words(text)
    chars_in_text = count_all_chars(text)
    sorted_chars = dict_to_list(chars_in_text)


    #Ausgabe der Textstatistik

    print("============ BOOKBOT ============")
    print("Analyzing book found at", filepath, "...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars :
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # isalpha prüft ob der char ein Buchstabe ist 
            print(f"{char}: {count}")

    print("============= END ===============")

main()