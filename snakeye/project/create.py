import os

from pathlib import Path
from snakeye.common.models import Project
from snakeye.common.toml import init_config
from snakeye.common.utils import parse_template


def create_new_project(project: Project):
    ctx = project.to_ctx()

    home = str(Path.home())

    # create __init__.py
    init_py = parse_template(home + "/.snakeye/template/__init__.txt", ctx)
    # create snakeye config files
    cfg = init_config(project)
    # create readme from template
    readme = parse_template(home + "/.snakeye/template/readme.txt", ctx)

    # create folder
    path = "./" + project.name
    os.mkdir(path)
    os.mkdir(path + "/" + project.name)

    file = open(path + "/" + project.name + "/__init__.py", "w")
    file.write(init_py)
    file.close()

    file = open(path + "/README.md", "w")
    file.write(readme)
    file.close()

    file = open(path + "/pyproject.toml", "w")
    file.write(cfg)
    file.close()

    if project.license_type in ["mit", "apache", "gpl"]:
        license_file = parse_template(home + '/.snakeye/template/license/' + project.license_type + '.txt', ctx)

        file = open(path + "/LICENSE", "w")
        file.write(license_file)
        file.close()
