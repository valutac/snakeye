from cleo import Command

from snakeye.project.build import build_project


class BuildProject(Command):
    """
    Build Current Project

    build
    """

    def handle(self):
        r = build_project()
        if r == 1:
            print("Build Failed")
