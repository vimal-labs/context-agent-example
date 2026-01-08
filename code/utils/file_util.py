import os
from typing import Optional

class FileUtil:
    """
    Utility class for file operations.
    """

    @staticmethod
    def read_file(file_path: str, encoding: str = "utf-8") -> Optional[str]:
        """
        Reads the content of a file and returns it as a string.
        Supports absolute paths and project-root-relative paths (starting with '/').

        Args:
            file_path (str): The path to the file. If it starts with '/', it is considered relative to the project root.
            encoding (str): The encoding to use when reading the file. Default is 'utf-8'.

        Returns:
            Optional[str]: The content of the file, or None if the file does not exist.
        """
        # If path starts with '/', treat as project-root-relative
        if file_path.startswith("/"):
            # Get the project root (two levels up from this file)
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            abs_path = os.path.join(project_root, file_path.lstrip("/\\"))
        else:
            abs_path = file_path

        try:
            with open(abs_path, 'r', encoding=encoding) as file:
                return file.read()
        except FileNotFoundError:
            print(f"File not found: {abs_path}")
            return None
        except Exception as e:
            print(f"Error reading file {abs_path}: {e}")
            return None
