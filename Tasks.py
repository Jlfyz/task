import re


def donuts(count):
    if count.isnumeric():
        if int(count) > 9:
            return 'Number of donuts: {0}'.format('many')
        else:
            return 'Number of donuts: {0}'.format(count)
    else:
        print('Incorrect use just integer nums')
        return donuts(input('Enter a num of donuts '))


counter = input('Enter a num of donuts ')
print(donuts(counter))


def both_ends(my_string):
    if len(my_string) < 2:
        return ''
    else:
        return f'{my_string[:2]}{my_string[len(my_string) - 2:]}'


string = input("Input string ")
print(both_ends(string))


def fix_start(my_string):
    return '{0}{1}'.format(my_string[0],
                           my_string[1:].replace(my_string[0], '*'))


s = input('Enter a word ')
print(fix_start(s))


def mix_up(first_word, second_word):
    if len(first_word) > 2 and len(second_word) > 2:
        return f'{second_word[:2]}{first_word[2:]} {first_word[:2]}{second_word[2:]}'
    else:
        print('It\'s wrong, because you used word with just 2 characters or less')


a = input('first word ')
b = input('second word ')
print(mix_up(a, b))


def del_all_aeiou(my_string):
    pattern = r"[aeiou]"
    if re.search(pattern, my_string):
        my_string = my_string.replace('a', '')
        my_string = my_string.replace('e', '')
        my_string = my_string.replace('i', '')
        my_string = my_string.replace('o', '')
        my_string = my_string.replace('u', '')
    return my_string


string = input('Some string ')

print(del_all_aeiou(string))


if __name__ == '__main__':
    print('Program started')