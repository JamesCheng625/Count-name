import os
from pathlib import Path


def count_names_from_content(content):
    """Core logic to count names from a string content."""
    raw_data = [line.strip() for line in content.splitlines()]

    input_data = [line for line in raw_data if line and line != '"']

    total_names = len(input_data)
    name_count = {}

    for name in input_data:
        name_count[name] = name_count.get(name, 0) + 1

    repeated_names = {name: count for name, count in name_count.items() if count > 1}
    unique_names_count = len(name_count)

    return {
        "total_names": total_names,
        "repeated_names": repeated_names,
        "unique_names_count": unique_names_count,
        "name_count": name_count,
        "sorted_unique_names": sorted(name_count.keys()),
    }


def count_names_from_file(filename):
    """File-based wrapper for the core logic."""
    file_path = Path(filename)
    if not file_path.exists():
        try:
            file_path.touch()
            return f"File '{filename}' did not exist. Created a new empty file."
        except Exception as e:
            return f"Error creating file: {e}"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return count_names_from_content(content)
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    print("This file now contains core logic. Use app.py for the Web UI.")
