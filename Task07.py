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


if __name__ == '__main__':
    my_string = input('Your string here ')
    print(not_bad(my_string))