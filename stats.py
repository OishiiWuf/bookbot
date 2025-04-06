def get_num_words(book_string):
    word_list = str.split(book_string)
    words_number = len(word_list)
    return words_number

def get_num_characters(book_string):
    character_count = {}
    for word in str.split(book_string):
        for character in word:
            char = str.lower(character)
            if(char not in character_count):
                character_count[char] = 1
            else:
                character_count[char] += 1
    return character_count

def get_sorted_list(dic_of_char):
    sorted_list = []
    for char in dic_of_char:
        char_dic = {
            "character": char,
            "count": dic_of_char[char]
        }
        sorted_list.append(char_dic)
    sorted_list.sort(reverse=True, key=sort_count)
    return sorted_list
    
def sort_count(dict):
    return dict["count"]
