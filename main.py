import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list


def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
   
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book1> [path_to_book2] [path_to_book3] ...")
        sys.exit(1)
    
    for filepath in sys.argv[1:]:
        process_book(filepath)

def process_book(filepath):
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    try:
        text = get_book_text(filepath)
        
        word_count = count_words(text)
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        
        char_counts = count_characters(text)
        
        sorted_chars = chars_dict_to_sorted_list(char_counts)
        
        print("--------- Character Count -------")
        for char_dict in sorted_chars:
            for char, count in char_dict.items():
                print(f"{char}: {count}")
        
        print("============= END ===============")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
    except Exception as e:
        print(f"Error processing file '{filepath}': {e}")

main()