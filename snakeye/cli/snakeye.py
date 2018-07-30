from cleo import Application

from snakeye.cli.command.add_dep import AddDep
from snakeye.cli.command.build_project import BuildProject
from snakeye.cli.command.list_dep import ListDep
from snakeye.cli.command.publish_project import PublishProject
from .command.create_project import CreateProject

application = Application()
application.add(CreateProject())
application.add(BuildProject())
application.add(PublishProject())
application.add(ListDep())
application.add(AddDep())
