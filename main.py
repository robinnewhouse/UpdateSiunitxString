"""
Working on my thesis and copying LaTeX from internal documentation source to thesis source.
The internal documentation didn't use the siunitx package, but I am, and find that I am updating strings by hand a lot.
I made this script as a way to convert the string quickly and to avoid mistyping the numerical value and unit.
"""


def update_string():
    old_string = input("Pase LaTeX string:")
    if '$' in old_string:
        math_mode(old_string)

    else:
        regular_string(old_string)


def math_mode(old_string):
    print(old_string)
    tokens = old_string.split('$')
    units = tokens[-1].strip('~')
    math_string = tokens[-2]
    numerical_value = []
    index = 0
    for i in range(1, len(math_string) + 1):
        if not math_string[-i].isnumeric(): break
        numerical_value.append(math_string[-i])
        index = i
    numerical_value.reverse()
    print()
    print(f'${math_string[0:-index]}\SI{{{"".join(numerical_value)}}}{{\\{units}}}$')


def regular_string(old_string):
    index = 0
    for i, x in enumerate(old_string):
        if not x.isnumeric():
            break
        else:
            index = i + 1
    print(f'\SI{{{old_string[0:index]}}}{{\\{old_string[index:].strip("~").strip(" ")}}}')


if __name__ == '__main__':
    update_string()
