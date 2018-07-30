from cleo import Command
from snakeye.dep.list import get_cfg, get_dependencies, flit_metadata, snakeye_metadata, display_deps


class ListDep(Command):
    """
    List Dependencies of the Project

    dep
    """

    def handle(self):
        path = "./pyproject.toml"
        cfg = get_cfg(path)
        flit = flit_metadata(cfg)
        snakeye = snakeye_metadata(cfg)
        deps = get_dependencies(cfg)
        display_deps(flit, snakeye, deps)
