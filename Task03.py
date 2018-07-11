def fix_start(my_string):
    return '{0}{1}'.format(my_string[0],
                           my_string[1:].replace(my_string[0], '*'))


def main():
    string = input('Enter a word ')
    print(fix_start(string))


if __name__ == 'main':
    main()