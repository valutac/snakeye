from cleo import Command
from snakeye.project.publish import publish_project


class PublishProject(Command):
    """
    Publish Current Project

    publish
    """

    def handle(self):
        r = publish_project()
        if r == 1:
            print("Publish Failed")
