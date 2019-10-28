from pathlib import Path
import jsonschema
from jsonschema import Draft7Validator
import json

OPTIMIZATION_PROJECT_SCHEMA = Path(__file__).resolve().parent.parent / "optimization" / "optimization_project.json"
OPTIMIZATION_PROJECT_DATA = Path(__file__).resolve().parent / "testing_schemas" / \
                            "rio_primero-example-optimization-start-request.json"


def test_optimization_project_schema_format():
    with open(OPTIMIZATION_PROJECT_SCHEMA) as f:
        loaded_schema = json.load(f)

    with open(OPTIMIZATION_PROJECT_DATA) as f:
        loaded_data = json.load(f)

    assert jsonschema.Draft7Validator(loaded_schema).validate(loaded_data)
    # assert Draft7Validator(loaded_schema).check_schema()
