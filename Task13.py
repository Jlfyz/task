def linear_merge(list1, list2):
    result = []
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result.extend(list1)
    result.extend(list2)
    return result


def main():
    list1 = [1, 3, 5, 7, 10]
    list2 = [2, 4, 6, 8, 9]
    print(linear_merge(list1, list2))


if __name__ == '__main__':
    main()
