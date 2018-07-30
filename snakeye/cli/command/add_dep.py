from cleo import Command

from snakeye.common.toml import update_config
from snakeye.dep.add import add_dep


class AddDep(Command):
    """
    Add Dependency to Current Project

    add
        {name? : Dependency Name?}
        {version? : Version Number?}
    """

    def handle(self):
        path = "./pyproject.toml"
        name = self.argument('name')
        version = self.argument('version')
        cfg = add_dep(path, name, version=version)
        cfg = update_config(cfg)
        file = open("pyproject.toml", "w")
        file.write(cfg)
        file.close()
