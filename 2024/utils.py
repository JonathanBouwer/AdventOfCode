import os

def parse_string(line):
    return line.strip()

def parse_int(line):
    return int(line.strip())

def load_input(script_name=None, parse_func=parse_string):
    """Helper function to load input based on file name"""
    if script_name is None:
        raise Exception("script_name is None. Pass in __file__")
    
    base_file_name = os.path.basename(script_name)
    base_name = base_file_name.split('.')[0].split('-')[0]
    input_file_name = base_name + '-input.txt'
    result = []
    try:
        with open(input_file_name, 'r') as data:
            result = [parse_func(line) for line in data.readlines()]
    except FileNotFoundError:
        print("Could not find file " + input_file_name)
    return result