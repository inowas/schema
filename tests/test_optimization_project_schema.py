import pytest
from pathlib import Path, PurePosixPath
import jsonschema
from jsonschema import RefResolver
import json
from copy import deepcopy

OPTIMIZATION_PROJECT_SCHEMA = Path(__file__).resolve().parent.parent / "optimization" / "optimization_project.json"
OPTIMIZATION_PROJECT_DATA = Path(__file__).resolve().parent / "testing_data" / \
                            "rio_primero-example-optimization-start-request.json"

schema_path = Path(OPTIMIZATION_PROJECT_SCHEMA).absolute()

with open(OPTIMIZATION_PROJECT_SCHEMA) as f:
    loaded_schema = json.load(f)

with open(OPTIMIZATION_PROJECT_DATA) as f:
    loaded_data = json.load(f)


def test_optimization_project_schema():
    """ Test validation of a valid data file against the jsonschema
    """
    test_schema = deepcopy(loaded_schema)
    test_data = deepcopy(loaded_data)

    path_resolver = RefResolver(base_uri=str(PurePosixPath('file://') / schema_path), referrer=test_schema)

    assert jsonschema.validate(test_data, test_schema, resolver=path_resolver) is None


def test_schema_ref():
    """ Test wrong reference path
    """
    test_schema = deepcopy(loaded_schema)
    test_data = deepcopy(loaded_data)

    test_schema["properties"]["data"]["$ref"] = "bla"

    path_resolver = RefResolver(base_uri=str(PurePosixPath('file://') / schema_path), referrer=test_schema)

    with pytest.raises(jsonschema.RefResolutionError):
        jsonschema.validate(test_data, test_schema, resolver=path_resolver)
