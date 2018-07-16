#!/usr/bin/python
import sys
import re


def extract_names(filename):
    with open(filename, 'r')as f:
        my_string = f.read()
    first_result = re.sub(r'<[^>]*>', '', my_string)
    year = re.findall(r'\d{4}', first_result)
    rank = re.findall(r'(\d+)[A-Z][A-Za-z]+[A-Z][A-Za-z]+', first_result)
    boy_name = re.findall(r'\d+([A-Z][A-Za-z]+)[A-Z][A-Za-z]+', first_result)
    girl_name = re.findall(r'\d+[A-Z][A-Za-z]+([A-Z][A-Za-z]+)', first_result)
    i = 0
    answer = [year[1]]
    for num in rank:
        boy_name[i] = boy_name[i]+' '+rank[i]
        girl_name[i] = girl_name[i]+' '+rank[i]
        answer.append(boy_name[i])
        answer.append(girl_name[i])
        i = i + 1
    return sorted(answer)


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: ./babynames.py [--summaryfile] file [file ...]')
        sys.exit(1)
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        with open(args[0], 'w')as summaryfile:
            summaryfile.write(str(extract_names(args[1])))
        del args[0]
    else:
        print(extract_names(args[0]))


if __name__ == '__main__':
    main()
