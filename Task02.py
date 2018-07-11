def both_ends(my_string):
    if len(my_string) < 2:
        return ''
    else:
        return '{0}{1}'.format(my_string[:2],
                               my_string[len(my_string) - 2:])


def main():
    string = input("Input string ")
    print(both_ends(string))


if __name__ == '__main__':
    main()
