from tomlkit import parse


def add_dep(path):
    # read toml file
    with open(path, "r") as f:
        text = parse(f)
    # extract toml file, packages listing
    # add to array if not exists
    # update path
    print(path)
