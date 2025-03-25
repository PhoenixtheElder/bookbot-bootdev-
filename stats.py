#STATS.PY


#liest den Text aus der Datei und ihn als string zurück
def read_book(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

#zählt die Wörter in einem gegebenen Text und gibt als int zurück
def count_words(text):
    wordlist = []
    wordlist = text.split()
    return len(wordlist) 

#konvertiert alle einzelnen Zeichen in einem Text zu lower case und gibt die Anzahl als dict zurück
def count_all_chars(text):
    charlist = {}
    for char in text.lower():
        charlist[char] = charlist.get(char, 0 ) + 1
    return charlist

#macht aus den gesammelten Daten von "count all chars" eine liste
def dict_to_list(chars_in_text):
    char_list = []
    for char, count in chars_in_text.items():
        char_list.append({"char" : char, "count" : count})
    
    #Hilfsfunktion für die geoordnete Liste
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list