def mix_up(first_word, second_word):
    return '{0}{1} {2}{3}'.format(second_word[:2], first_word[2:],
                                  first_word[:2], second_word[2:])


def main():
    while True:
        first_word = input('first word ')
        second_word = input('second word ')
        if len(first_word) > 2 and len(second_word) > 2:
            print(mix_up(first_word, second_word))
            break
        else:
            print('It\'s wrong, because you used word with just 2 characters or less')


if __name__ == '__main__':
    main()

