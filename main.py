from stats import count_words

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    

 
def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    
main()