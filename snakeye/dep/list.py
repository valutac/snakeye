import pytoml as toml


def get_cfg(path):
    # read config file
    with open(path, "r") as f:
        cfg = toml.load(f)

    return cfg


def flit_metadata(cfg):
    return cfg.get("tool").get("flit").get("metadata")


def snakeye_metadata(cfg):
    return cfg.get("tool").get("snakeye").get("metadata")


def get_dependencies(cfg):
    return cfg.get("tool").get("snakeye").get("dependencies")


def display_deps(flit, snakeye, deps):
    print(flit, snakeye, deps)
    print("{} {} {}".format(flit["module"], snakeye["pkg_version"], snakeye["description"]))
    print()
    print("Dependencies: ")
    length = len(deps)
    i = 1
    for dep, version in deps.items():
        if i == 1:
            print("├── {} {}".format(dep, version))
        elif i == length:
            print("└── {} {}".format(dep, version))
        else:
            print("├── {} {}".format(dep, version))
        i += 1
