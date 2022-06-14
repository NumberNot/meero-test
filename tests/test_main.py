import pytest

# Quirky test
@pytest.fixture
def file_name():
    return("log.txt")

def test_file_name(file_name):
    print(file_name)
    assert len(file_name) == 7, 'Possible wrong file'
    assert file_name == "log.txt", 'Wrong file'

# Presence test
@pytest.fixture
def file_content():
    file_name = "log.txt"
    file = open(file_name, "r")
    data = []
    process = ["date", "operation", "name", "condition"]
    for line in file.readlines():
        details = line.split(" ")
        details = [x.strip() for x in details]
        structure = {key: value for key, value in zip(process, details)}
        data.append(structure)
    return(data)


def test_file_content(file_content):
    print(file_content)
