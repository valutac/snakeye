import shlex
from subprocess import call


def publish_project(cwd=None, repository="pypitest"):
    args = shlex.split("flit --repository {} publish".format(repository))
    return call(args, cwd=cwd)
