import re


def del_all_vowels_letters(my_string):
    pattern = r"[aeiou]"
    if re.search(pattern, my_string):
        my_string = my_string.replace('a', '')
        my_string = my_string.replace('e', '')
        my_string = my_string.replace('i', '')
        my_string = my_string.replace('o', '')
        my_string = my_string.replace('u', '')
    return my_string


def main():
    string = input('Some string ')
    print(del_all_vowels_letters(string))


if __name__ == 'main':
    main()
