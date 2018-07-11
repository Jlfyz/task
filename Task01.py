def donuts(count):
    if int(count) > 9:
        return 'Number of donuts: {0}'.format('many')
    else:
        return 'Number of donuts: {0}'.format(count)


if __name__ == '__main__':
    while True:
        counter = input('Enter a num of donuts ')
        if counter.isnumeric():
            print(donuts(counter))
            break
        else:
            print('Incorrect use just integer nums')