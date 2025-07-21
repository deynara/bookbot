def main():
    book_path = "books/frankenstein.txt"
    #book_path = "books/test.txt"
    #book_path = "books/empty.txt"

#resulting print    
    print(f"Analyzing {book_path}")
    text = get_book_text(book_path)
    word_count = count_words(text) #type = string
    char_count = count_chars(text) #type = dictionary
    print(f"--- Begin report of {book_path} ---")
    print(word_count, 'words found')
    #print('The document contains these characters (in lower case):','\n',  char_count)
    char_report(char_count,True,True) #optinal Boolean for sort_by_amount and only_include_letters.

#functions
def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = len(text.split())
    return count

def count_chars(text, LCase = True):
    chars_count = {}  
    if LCase:
        text_lc = text.lower()
    else:
        text_lc = text
    #create a set of every character in the string and elimites duplicates due to the inherent uniqueness of sets, then convert it into a list to sort it in ascending order
    chars_list = sorted(list(set(text_lc))) 
    for char in chars_list:
        chars_count[char] = len(text_lc) - len(text_lc.replace(char,"")) #count is equal to length of original text minus length of text with every instance of char removed
    
    return chars_count
    
def char_report(Dict, Amount = True, Alphabet_Only = True):
    print("These characters were found:", "\n")
    #line break message
    if "\n" in Dict:
        count = Dict["\n"]
        print(f"A line break occured {count} times.")
    else:
        print(f"No line breaks were encountered.")
    #choice sorted by amount or character
    if Amount:
        sort_Dict = Sort_Dict_by_Value(Dict) #sort dictonary by values
    else:
        sort_Dict = Dict

    #print the report
    for key in sort_Dict:
        count = sort_Dict[key]
        if key == "\n":
            pass
        else:
            if not Alphabet_Only or str(key).isalpha():
                print(f"'{key}' {count} times")
            pass

def Sort_Dict_by_Value(Dict):
    #convert dictionary into a list of tuples
    Dict_List = []
    for key in Dict:
        new_Tupel = Dict[key], key
        Dict_List.append(new_Tupel) 
    
    #sort list
    Dict_List = sorted(Dict_List,reverse=True) 
    #reasign tuples list to dictionary
    sort_Dict = {}
    for item in Dict_List: 
       sort_Dict[item[1]] = item[0]

    return sort_Dict

main()