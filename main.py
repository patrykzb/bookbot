def main():
    book = "./books/frankenstein.txt"
    text = read(book)
    print(f'--- Begin report of {book} ---')
    count_words(text)
    count_letters(text)
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
        if letter in dict_letters:
            dict_letters[letter] += 1
        else:
            dict_letters[letter] = 1

    for letter in dict_letters:
        if letter.isalpha():
            print(f"The {letter} character was found {dict_letters[letter]} times")
    return dict_letters



main()