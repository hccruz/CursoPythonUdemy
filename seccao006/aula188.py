# argparse.ArgumentParser para argumentos complexos
# Tutorial Oficial:
# https://docs.python.org/3/library/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-b', '--basic')

args = parser.parse_args()
print(args.basic)
