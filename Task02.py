def both_ends(my_string):
    if len(my_string) < 2:
        return ''
    else:
        return '{0}{1}'.format(my_string[:2],
                               my_string[len(my_string) - 2:])


if __name__ == '__main__':
    string = input("Input string ")
    print(both_ends(string))
