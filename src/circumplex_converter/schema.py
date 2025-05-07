from jsonschema import validate
CIRCUMPLEX_SCHEMA={'type':'array'}  # shortened for demo
def validate_json(data):
    validate(data,CIRCUMPLEX_SCHEMA)