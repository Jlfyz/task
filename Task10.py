def front_x(words, x_words):
    printed_list = []
    x_words.sort(key=lambda x_word: x_word[1])
    words.sort(key=lambda word: word[-1])
    for x_word in x_words:
        printed_list.append(x_word)
    for word in words:
        printed_list.append(word)
    return printed_list


def main():
    words = []
    x_words = []
    count = int(input('Counter  of strings '))
    while count >= 1:
        count -= 1
        your_input = input('Your word here ')
        if your_input.startswith('x'):
            x_words.append(your_input)
        else:
            words.append(your_input)
    print(front_x(words, x_words))


if __name__ == '__main__':
    main()