def main():
    book = "./books/frankenstein.txt"
    text = read(book)
    print(f'--- Begin report of {book} ---')
    count_words(text)
    x = count_letters(text)
    list_letters(x)
    print("--- End report ---")



def read(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
        words = text.split()
        print(f'{len(words)} words found in the document')

def count_letters(text):
    small_letters = text.lower()
    l = list(small_letters)
    dict_letters = {}
    for letter in l:
        if letter.isalpha():
            if letter in dict_letters:
                dict_letters[letter] += 1
            else:
                dict_letters[letter] = 1
    return dict_letters

def sort_on(dict_letters):
    return dict_letters['num']

def list_letters(dict_letters):
    sorted_list = []
    for letter in dict_letters:
        sorted_dict = {'char': letter, 'num': dict_letters[letter]}
        sorted_list.append(sorted_dict)
    sorted_list = sorted(sorted_list, key=sort_on, reverse=True)
    for sorted_dict in sorted_list:
        print(f"The character '{sorted_dict['char']}' was found {sorted_dict['num']} times")




main()