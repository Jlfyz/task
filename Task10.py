def front_x(words):
    x_list = []
    list = []
    for word in words:
        if word.startswith('x'):
            x_list.append(word)
        else:
            list.append(word)
    return sorted(x_list) + sorted(list)


def main():
    words = []
    x_words = []
    while True:
        count = input('Count of strings ')
        if count.isdecimal():
            count = int(count)
            break
        else:
            continue
    while count >= 1:
        count -= 1
        words.append( input('Your word here '))
    print(front_x(words))


if __name__ == '__main__':
    main()