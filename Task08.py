def front_back(first_word, second_word):
    first_word_len = len(first_word)
    second_word_len = len(second_word)
    if first_word_len % 2 == 0:
        first_word_index = first_word_len // 2
    else:
        first_word_index = (first_word_len // 2) + 1
    if second_word_len % 2 == 0:
        second_word_index = second_word_len // 2
    else:
        second_word_index = (second_word_len // 2) + 1
    first_word_front = first_word[0:first_word_index]
    first_word_back = first_word[first_word_index:]
    second_word_front = second_word[0:second_word_index]
    second_word_back = second_word[second_word_index:]
    return first_word_front + second_word_front + first_word_back + second_word_back


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
