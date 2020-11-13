import ast
import json
from os.path import join, dirname


def assert_valid_json_schema(data, schema_file):
    """ Checks whether the given data matches the schema """
    return data == _load_json_schema(schema_file)

def get_valid_json_schema(schema_file):
    return _load_json_schema(schema_file)

def assert_valid_dictionary_schema(data, schema_file):
    return data == _load_dictionary_schema(schema_file)

def get_valid_dictionary_schema(schema_file):
    return _load_dictionary_schema(schema_file)

def get_xml_file(schema_file):
    return _load_xml(schema_file)

def _load_json_schema(filename):
    """ Loads the given schema file """

    relative_path = join('schemas', filename)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())


def _load_dictionary_schema(filename):
    relative_path = join('schemas', filename)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        return ast.literal_eval(schema_file.read())

def _load_xml(filename):
    relative_path = join('schemas', filename)
    absolute_path = join(dirname(__file__), relative_path)
    with open(absolute_path) as schema_file:
        return schema_file.read()