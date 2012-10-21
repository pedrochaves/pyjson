from stringifier import stringify

def to_file(file_name, obj):
    with open(file_name, "w+") as f:
        f.write(stringify(obj))
