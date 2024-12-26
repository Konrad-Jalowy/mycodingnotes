import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", action="store")

args = parser.parse_args()

print(args.url)