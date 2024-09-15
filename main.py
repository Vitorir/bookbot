def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    # words = return_words(text)
    # print(words)
    # print(f'Number of words in the book: {len(return_words(text))}')
    dic = number_of_times_character_appears_dict(text)

    list_of_dicts = [{'key': key, 'num': value} for key, value in dic.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    print(list_of_dicts)


def get_book_text(path):
    with open(path) as f:
       return f.read()

def return_words(text):
    return text.split()

def number_of_times_character_appears_dict(text):
    characters = {}
    for character in 'abcdefghijklmnopqrstuvwxyz':
        characters[character] = text.count(character)
    return characters

def sort_on(dict):
    return dict['num']
    

main()
