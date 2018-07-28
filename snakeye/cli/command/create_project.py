import os

from cleo import Command

from snakeye.common.utils import ask_input, parse_template


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

        ctx = {
            'pkg_name': name,
            'pkg_version': version,
            'author': author,
            'author_email': email,
            'description': description,
            'long_description': long_description,
            'url': url,
        }

        readme = parse_template("snakeye/template/readme.txt", ctx)
        setup = parse_template("snakeye/template/setup.txt", ctx)

        # create folder
        path = "./target/" + name
        os.mkdir(path)
        os.mkdir(path + "/" + name)
        open(path + "/" + name + "/__init__.py", "w").close()

        file = open(path + "/README.md", "w")
        file.write(readme)
        file.close()

        file = open(path + "/setup.py", "w")
        file.write(setup)
        file.close()

        if license_type in ["mit", "apache", "gpl"]:
            license_file = parse_template('template/license/' + license_type + '.txt', ctx)

            file = open(path + "/LICENSE", "w")
            file.write(license_file)
            file.close()
