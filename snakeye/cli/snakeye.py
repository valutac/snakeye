from cleo import Application

from .command.create_project import CreateProject

application = Application()
application.add(CreateProject())
