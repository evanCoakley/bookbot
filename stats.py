def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    text = text.lower()
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count

def chars_dict_to_sorted_list(char_counts):
    result = []
    for char, count in char_counts.items():
        if char.isalpha():
            result.append({char: count})
            
    result.sort(key=lambda x: list(x.values())[0], reverse=True)
        
    return result