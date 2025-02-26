from stats import get_book_text
from stats import characters_counter
from stats import words_counter
from stats import sorting_list
import sys


def main():
    if len(sys.argv) < 1: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words_counter(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")

    list = sorting_list(characters_counter(get_book_text(sys.argv[1])))
    for i in list:
        for item in i:
            if item.isalpha() == True:
                print(f"{item}: {i[item]}")
    print("============= END ===============")
    
main()
