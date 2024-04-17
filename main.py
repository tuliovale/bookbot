def main():
    path = 'books/frankestein.txt'
    print(f"-- Begin report of {path} ---")
    with open('books/frankestein.txt') as f:
        file_contents = f.read()
    letters = sort_dict(count_letters(file_contents))
    for letter in letters:
        print(f"The {letter['letter']} character was found {letter['num']} times")
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list_dicts = []
    for letter in dict:
        list_dicts.append({'letter' : letter, 'num' : dict[letter]})
    print(list_dicts)
    list_dicts.sort(reverse=True, key=sort_on)
    return list_dicts

def count_letters(text):
    letters = {}
    for letter in text:
        if letter.isalpha():
            lowercase = letter.lower()
            if lowercase in letters:
                letters[lowercase] += 1
            else:
                letters[lowercase] = 1
    return letters


main()