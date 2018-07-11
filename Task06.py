def verbing(verb_string):
    if 3 <= len(verb_string):
        if verb_string[len(verb_string) - 3:] == 'ing':
            verb_string = '{0}{1}'.format(verb_string, "ly")
            return verb_string
        else:
            verb_string = '{0}{1}'.format(verb_string, "ing")

            return verb_string
    else:
        return verb_string


if __name__ == '__main__':
    string = input('Hello your word here ')
    print(verbing(string))