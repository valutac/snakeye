from cleo import Command

from snakeye.common.models import Project
from snakeye.common.utils import ask_input
from snakeye.project.create import create_new_project


class CreateProject(Command):
    """
    Create New Project

    create
        {name? : Project Name?}
    """

    def handle(self):
        name = self.argument('name')
        version = ask_input("What's version number: ")
        author = ask_input('Author Name: ')
        email = ask_input('Author Email: ')
        description = ask_input('Description: ')
        long_description = ask_input('Long Description: ')
        url = ask_input('URL/Homepage: ')
        license_type = ask_input('License (mit / apache / gpl / leave blank for empty license): ')

        project = Project(name=name, version=version, author=author, email=email, description=description,
                          long_description=long_description, url=url, license_type=license_type)
        create_new_project(project)

        print("Make sure to add VCS in your projects to enable build and publish")
