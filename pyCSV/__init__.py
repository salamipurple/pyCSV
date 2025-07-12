import csv
import os

class pyCSV:
    _files_written = set()
    file_path = None

    @classmethod
    def new(cls, name, path=""):
        if path.strip() == "":
            base_path = os.getcwd()  # parent folder of where u run script
        else:
            base_path = os.path.abspath(path)
        os.makedirs(base_path, exist_ok=True)
        full_path = os.path.join(base_path, f"{name}.csv")
        cls.file_path = full_path
        cls._files_written.discard(full_path)  # reset so headers write fresh next time
        return full_path

    @classmethod
    def append(cls, file_name, *args):
        need_header = not os.path.exists(file_name) and file_name not in cls._files_written
        mode = "w" if need_header else "a"
        with open(file_name, mode, newline="") as f:
            writer = csv.writer(f)
            if need_header:
                headers = [f"column{i+1}" for i in range(len(args))]
                writer.writerow(headers)
                cls._files_written.add(file_name)
            writer.writerow(args)