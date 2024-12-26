import argparse
import validators
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", action="store")

args = parser.parse_args()

url = args.url


def add_protocol(_url):
    if _url.startswith("https://") or _url.startswith("http://"):
        return url
    return "https://" + url


def is_url(_url):
    return True if validators.url(_url) else False


def main():
    print("Main function running")


def check_before_run():
    global url
    url = add_protocol(url)
    if not is_url(url):
        print("Not an url!")
        sys.exit()


if __name__ == '__main__':
    check_before_run()
    main()