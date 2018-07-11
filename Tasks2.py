def verbing(verb_string):
    if 3 <= len(verb_string):
        if verb_string[len(verb_string) - 3:] == 'ing':
            verb_string = f'{verb_string}{"ly"}'
            return verb_string
        else:
            verb_string = f'{verb_string}{"ing"}'

            return verb_string
    else:
        return verb_string


string = input('Hello your word here ')

print(verbing(string))


def not_bad(working_string):
    if 'not' in working_string and 'bad' in working_string:
        if working_string.find('not') < working_string.find('bad'):
            return '{0}{1}'.format(working_string[:working_string.find('not')],
                                   'good')
        else:
            working_string = working_string.replace('not',
                                                    '')
            working_string = working_string.replace('bad',
                                                    'good')
            return working_string
    else:
        return 'In string \'{0}\' is not find not or bad'.format(working_string)


my_string = input('Your string here ')
print(not_bad(my_string))


def front_back(first_word, second_word):
    if len(first_word) >= 2 and len(second_word) >= 2:
        if len(first_word) % 2 != 0:
            first_part_of_first_word = first_word[:int(len(first_word) / 2) + 1]
            second_part_of_first_word = first_word[int(len(first_word) / 2) + 1:]
        if len(first_word) % 2 == 0:
            first_part_of_first_word = first_word[:int(len(first_word) / 2)]
            second_part_of_first_word = first_word[int(len(first_word) / 2):]
        if len(second_word) % 2 != 0:
            first_part_of_second_word = second_word[:int(len(second_word) / 2) + 1]
            second_part_of_second_word = second_word[int(len(second_word) / 2) + 1:]
        if len(second_word) % 2 == 0:
            first_part_of_second_word = second_word[:int(len(second_word) / 2)]
            second_part_of_second_word = second_word[int(len(second_word) / 2):]
        return '{0}{1}{2}{3}'.format(first_part_of_first_word,
                                     first_part_of_second_word,
                                     second_part_of_first_word,
                                     second_part_of_second_word)
    else:
        print('Wrong try again!')
        return front_back(input('First word here: '),
                          input('Second word here: '))


a = input('First word here: ')

b = input('Second word here: ')

print(front_back(a, b))


if __name__ == '__main__':
    print('Program started')
