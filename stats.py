def count_words(text):
    count = len(text.split())
    return count

def count_chars(text, LCase = True):
    dict_chars = {}  
    if LCase:
        text_lc = text.lower()
    else:
        text_lc = text
    #create a set of every character in the string and elimites duplicates due to the inherent uniqueness of sets, then convert it into a list to sort it in ascending order
    chars_list = sorted(list(set(text_lc))) 
    for char in chars_list:
        dict_chars[char] = len(text_lc) - len(text_lc.replace(char,"")) #count is equal to length of original text minus length of text with every instance of char removed
    
    return dict_chars

def char_sort (dict_chars):
    dict_list = []
    for key in dict_chars:
        dict_list.append({"char":key, "value":dict_chars[key]})
    dict_list.sort(reverse=True, key=sort_on)
    #print (dict_list)
    return dict_list

def sort_on(items):
    return items["value"]
