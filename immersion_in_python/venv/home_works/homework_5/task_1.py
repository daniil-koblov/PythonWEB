file_path = "C:/Users/User/Documents/example.txt"

#  Решение

def get_file_info(file_path):
    file_name = file_path.split('/')[-1]
    file_expansion = file_name.split('.')[-1]
    path_before_file = file_path[: -len(file_name)]
    return (path_before_file, file_name[: -len(file_expansion) - 1], "." + file_expansion)

#  Эталонное решение

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)
