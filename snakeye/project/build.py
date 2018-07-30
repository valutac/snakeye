import shlex
from subprocess import call


def build_project(cwd=None):
    args = shlex.split("flit build")
    return call(args, cwd=cwd)
