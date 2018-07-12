def remove_adjacent(nums):
    result = []
    for num in nums:
        if len(result) == 0 or num != result[-1]:
            result.append(num)
    return result


def main():
    list_of_nums = []
    while True:
        count = input('Count of integers ')
        if count.isdecimal():
            count = int(count)
            break
        else:
            continue
    while count >= 1:
        count -= 1
        while True:
            your_input = input('Your number here ')
            if your_input.isdecimal():
                your_input = int(your_input)
                break
            else:
                continue
        list_of_nums.append(your_input)
    print(remove_adjacent(list_of_nums))


if __name__ == '__main__':
    main()

