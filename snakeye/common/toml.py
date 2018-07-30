import pytoml as toml

from snakeye.common.models import Project
from snakeye.dep.list import get_dependencies, flit_metadata, snakeye_metadata

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


def update_config(cfg):
    deps = get_dependencies(cfg)
    snakeye = snakeye_metadata(cfg)
    flit = flit_metadata(cfg)
    return TEMPLATE.format(metadata=toml.dumps(flit),
                           snakeye_metadata=toml.dumps(snakeye),
                           dependencies=toml.dumps(deps))
