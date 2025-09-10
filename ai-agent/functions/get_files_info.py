import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(path)
    rel_path_dir = os.path.relpath(path)
    if rel_path_dir not in abs_path:
        return f"Error: cannot list '{
            rel_path_dir
        }' as it is outside the permitted working directory"

    dir_list = os.listdir(abs_path)

    result = list()

    result.append("Result for current directory:")
    for entry in dir_list:
        entry_path = os.path.join(abs_path, entry)
        if os.path.isfile(entry_path):
            result.append(
                f"- {entry}: file_size={
                    os.path.getsize(entry_path)
                } bytes, is_dir=False"
            )
        else:
            nested_dir = os.listdir(entry_path)
            sum = 0
            for nested_entry in nested_dir:
                nested_entry_path = os.path.join(entry_path, nested_entry)
                if not os.path.isfile(nested_entry_path):
                    continue

                sum += os.path.getsize(nested_entry_path)

            result.append(f"- {entry}: file_size={sum} bytes, is_dir=True")

    return "\n".join(result)
