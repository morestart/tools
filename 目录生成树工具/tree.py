from pathlib import Path


tree_str = ''

ignore_dir = [
    ".pio",
    ".git",
    ".vscode",
    ".idea"
]

ignore_file = [
    "gitattributes",
    "gitignore",
    "yml",
    "travis",
]


def is_ignore_path(path):
    if path in ignore_dir:
        return True
    else:
        return False


def is_ignore_file(filename):
    # print(filename)
    out = filename.split('.')
    # print(out)
    try:
        if out[1] in ignore_file:
            return True
        else:
            return False
    except IndexError:
        pass


def generate_tree(pathname, n=0):
    global tree_str

    if pathname.is_file():
        if not is_ignore_file(pathname.name):
            tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'

    elif pathname.is_dir():
        # print(pathname)
        if not is_ignore_path(pathname.name):
            tree_str += '    |' * n + '-' * 4 + \
                str(pathname.relative_to(pathname.parent)) + '\n'
            for cp in pathname.iterdir():
                generate_tree(cp, n + 1)


if __name__ == '__main__':
    generate_tree(Path.cwd())
    print(tree_str)
