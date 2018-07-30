import pytoml as toml

from snakeye.common.models import Project

TEMPLATE = """\
[build-system]
requires = ["flit"]
build-backend = "flit.buildapi"

[tool.flit.metadata]
{metadata}

[tool.snakeye.dependencies]
{dependencies}
"""


def init_config(project: Project):
    return TEMPLATE.format(metadata=toml.dumps(project.to_flit_metadata()), dependencies=toml.dumps({}))
