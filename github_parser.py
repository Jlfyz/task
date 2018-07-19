from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.error import URLError
import re


class MyHTMLParser(HTMLParser):
    def __init__(self, site_name, *args, **kwargs):
        self.links = []
        self.site_name = site_name
        super().__init__(*args, **kwargs)
        self.feed(self.read_site_content())
        self.print_to_console()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    if not self.validate(attr[0]):
                        self.links.append(attr[1])

    def validate(self, link):
        return link in self.links or '#' in link or 'javascript:' in link

    def read_site_content(self):
        return str(urlopen(self.site_name).read())

    def print_to_console(self):
        return'\n'.join(sorted(self.links))

    def print_to_console_just_repositories(self, username):
        my_filter = r'\/'+username+'\/([A-Za-z0-9]+)'
        result = re.findall(my_filter, str(self.links))
        return '\n'.join(sorted(result))

    def print_readmemd(self):
        first_result = re.sub(r'<[^>]*>', '',  self.read_site_content())
        second_result = re.sub(r'b?\'', '', first_result)
        last_result = re.sub(r'\\n', '\\n', second_result)
        return last_result


def main():
    flag = input('Input key(1,2) 1 - give username and my program gives you list of repositories '
                 '2 - give url of your repository and my program logs README.MD without HTML tags ')
    if flag == '1':
        while True:
            try:
                username = input('Your username from github ')
                parser = MyHTMLParser("https://github.com/{0}".format(username))# ?tab=repositories
                print(parser.print_to_console_just_repositories(username))
                break
            except Exception as exc:
                print(str(exc))
                continue
    elif flag == '2':
        while True:
            try:
                username = input('Your Url (username/your repositorie/branch) ')
                url = 'https://raw.githubusercontent.com/' + username + '/README.md'
                matching_URL = re.match(r'(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?', url)
                if matching_URL is None:
                    print('Incorrect URL')
                    continue
                else:
                    parser = MyHTMLParser(url)
                    print(parser.print_readmemd())
                    break
            except Exception as e:
                print(str(e))
                continue
    else:
        print('wrong key')


if __name__ == '__main__':
    main()
