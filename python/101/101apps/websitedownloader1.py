import argparse
import validators
import sys
import os
import requests

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", action="store", required=True)
parser.add_argument("-o", "--out", action="store", required=False, default="websites")

args = parser.parse_args()

url = args.url
out = args.out


def add_protocol(_url):
    if _url.startswith("https://") or _url.startswith("http://"):
        return url
    return "https://" + url


def is_url(_url):
    return True if validators.url(_url) else False

def set_cwd():
    script_dir = os.path.dirname(__file__)
    os.chdir(script_dir)

def set_out_directory():
    _path = os.path.join(os.getcwd(), out)
    if not os.path.exists(_path):
        os.mkdir(out)

def main():
    print("Main function running")
    response = requests.get(url, allow_redirects=True)
    if response.ok:
        print("Website found")


def check_before_run():
    global url
    url = add_protocol(url)
    if not is_url(url):
        print("Not an url!")
        sys.exit()
    set_cwd()
    set_out_directory()

if __name__ == '__main__':
    check_before_run()
    main()