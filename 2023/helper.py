import os


def read_input(file_name):
    project_dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_dir_path, "data", file_name)

    with open(file_path, "r") as file:
        input = file.read()
    return input
