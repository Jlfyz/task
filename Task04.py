def mix_up(first_word, second_word):
    return '{0}{1} {2}{3}'.format(second_word[:2], first_word[2:],
                                  first_word[:2], second_word[2:])


if __name__ == '__main__':
    while True:
        a = input('first word ')
        b = input('second word ')
        if len(a) > 2 and len(b) > 2:
            print(mix_up(a, b))
            break
        else:
            print('It\'s wrong, because you used word with just 2 characters or less')
