import random


def print_hi(name):
    print(f'Hi, {name}')


def gen_number():
    return random.randint(1, 100)


def print_bye(name):
    print(f'Bye, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    print_bye('PyCharm')
