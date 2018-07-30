import shlex
from snakeye.common.exception import DuplicateDependencyException, InstallDependencyFailedException
from subprocess import Popen, PIPE, call

from .list import get_cfg, get_dependencies, set_dependencies


def add_dep(path, dep, version=None):
    # extract toml file, packages listing
    cfg = get_cfg(path)
    deps = get_dependencies(cfg)

    # add to array if not exists
    for installed in deps.keys():
        if installed.lower() == dep.lower():
            raise DuplicateDependencyException()

    if version:
        args = shlex.split("pip install {}=={}".format(dep, version))
    else:
        args = shlex.split("pip install {}".format(dep))

    # install dep
    r = call(args)
    if r == 1:
        raise InstallDependencyFailedException()

    p = Popen(shlex.split("pip freeze"), stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False)
    output, _ = p.communicate(b"input data that is passed to subprocess' stdin")
    if p.returncode == 1:
        raise InstallDependencyFailedException()

    for row in output.split(b'\n'):
        package = row.decode("utf-8").split('==')
        if len(package) == 0:
            continue
        if dep.lower() == package[0].lower():
            dep = package[0]
            deps[dep] = package[1]
            break

    if deps.get(dep, None) is None:
        raise InstallDependencyFailedException()

    cfg = set_dependencies(cfg, deps)

    return cfg
