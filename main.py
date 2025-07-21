import sys
import os
from stats import count_words
from stats import count_chars, char_sort

def main():
    print("Starting bookbot")
    
    #test = sys.argv
    #print (test)
    if len(sys.argv) != 2:
        print ("No bookpath given. \nUsage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    #test = book_path[-3:]
    #print(test)
    if not os.path.isfile(book_path) or book_path[-3:] != "txt":
        print (f"Found no textdocument at {book_path}. \nUsage: python3 main.py <path_to_book>")
        sys.exit(1) 
    #book_path = "books/frankenstein.txt"
    #book_path = "books/test.txt"
    #book_path = "books/empty.txt"
    print (f"Analyzing text in {book_path}")
    text = get_book_text(book_path)
    print_count(count_words(text))

    char_count = count_chars(text)
    print_chars(char_sort(count_chars(text)))
    

#functions
def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_count(count):
    print(f"Found {count} total words in the document")

def print_chars(sorted_char_dict_list):
    #print (sorted_char_dict_list)
    for char_dict in sorted_char_dict_list:
        char = char_dict["char"]
        if char.isalpha():
            value = char_dict["value"]
            print (f"{char}: {value}")


main()