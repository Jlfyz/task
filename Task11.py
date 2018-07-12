def sort_last(tuples):
    tuples.sort(key=lambda my_tuple: my_tuple[-1])
    return tuples


def main():
    print('sort_last')
    print(sort_last([(1, 3), (3, 2), (2, 1)]))
    print(sort_last([(2, 3), (1, 2), (3, 1)]))
    print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))


if __name__ == '__main__':
    main()