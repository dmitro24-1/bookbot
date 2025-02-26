def get_book_text(book):

    with open(book) as f:
        file_content = f.read()
    return file_content


def words_counter(string):
    counter = 0
    new_string = string.split()
    for i in new_string:
        counter += 1
    return counter


def characters_counter(string):
    characters = {"a" : 0,
                  "b" : 0,
                  "c" : 0,
                  "d" : 0,
                  "e" : 0,
                  "f" : 0,
                  "g" : 0,
                  "h" : 0,
                  "i" : 0,
                  "j" : 0,
                  "k" : 0,
                  "l" : 0,
                  "m" : 0,
                  "n" : 0,
                  "o" : 0,
                  "p" : 0,
                  "q" : 0,
                  "r" : 0,
                  "s" : 0,
                  "t" : 0,
                  "u" : 0,
                  "v" : 0,
                  "w" : 0,
                  "x" : 0,
                  "y" : 0,
                  "z" : 0,
                  " " : 0,
                  "." : 0,
                  "," : 0,
                  ":" : 0,
                  "!" : 0,
                  "?" : 0,
                  ";" : 0}
    new_string = string.lower()
    for item in new_string:
        for char in characters:
            if item == char:
                characters[char] += 1

    return characters

def sorting_list(dict):
    list = []
    for item in dict:
        list.append({item: dict[item]})
    def sort_on(dicty):
        for i in dicty:
            return dicty[i]
    list.sort(reverse = True, key = sort_on)
    return list

    
    
    