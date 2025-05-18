def write_file(file_name, file_content):
    pass
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'w', encoding='utf-8') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    pass
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'a', encoding='utf-8') as f:
        f.write(append_content)

def read_file(file_name):
    pass
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    return content
