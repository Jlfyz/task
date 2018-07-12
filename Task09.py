def match_ends(words):
    counter = 0
    for word in words:
        if 2 < len(word) and word[0] == word[-1]:
            counter += 1
    return counter


def main():
    words = []
    count = int(input('Count of strings '))
    while count >= 1:
        count -= 1
        words.append(input('Your word here '))
    print(match_ends(words))


if __name__ == '__main__':
    main()
