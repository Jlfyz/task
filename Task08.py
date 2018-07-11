def front_back(first_word, second_word):
    if len(first_word) % 2 != 0:
        first_part_of_first_word = first_word[:int(len(first_word) / 2) + 1]
        second_part_of_first_word = first_word[int(len(first_word) / 2) + 1:]
    elif len(first_word) % 2 == 0:
        first_part_of_first_word = first_word[:int(len(first_word) / 2)]
        second_part_of_first_word = first_word[int(len(first_word) / 2):]
    if len(second_word) % 2 != 0:
        first_part_of_second_word = second_word[:int(len(second_word) / 2) + 1]
        second_part_of_second_word = second_word[int(len(second_word) / 2) + 1:]
    elif len(second_word) % 2 == 0:
        first_part_of_second_word = second_word[:int(len(second_word) / 2)]
        second_part_of_second_word = second_word[int(len(second_word) / 2):]
    return '{0}{1}{2}{3}'.format(first_part_of_first_word,
                                 first_part_of_second_word,
                                 second_part_of_first_word,
                                 second_part_of_second_word)


def main():
    while True:
        first_word = input('First word here: ')
        second_word = input('Second word here: ')
        if len(first_word) >= 2 and len(second_word) >= 2:
            print(front_back(first_word, second_word))
            break
        else:
            print('Wrong try again!')


if __name__ == '__main__':
    main()
