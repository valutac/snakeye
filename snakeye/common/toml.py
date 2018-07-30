import pytoml as toml

from snakeye.common.models import Project

TEMPLATE = """\
[build-system]
requires = ["flit"]
build-backend = "flit.buildapi"

[tool.flit.metadata]
{metadata}

[tool.snakeye.metadata]
{snakeye_metadata}

[tool.snakeye.dependencies]
{dependencies}
"""


def init_config(project: Project):
    dependencies = {"flit": "1.0"}
    return TEMPLATE.format(metadata=toml.dumps(project.to_flit_metadata()),
                           snakeye_metadata=toml.dumps(project.to_ctx()),
                           dependencies=toml.dumps(dependencies))
