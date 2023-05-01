import sys
import os

MIN_NUM_ARGS = 4


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def validate_input_path(input_path):
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' does not exist.")
        sys.exit(1)


def reverse_file_content(input_path, output_path):
    content = read_file(input_path)
    reversed_content = content[::-1]
    write_file(output_path, reversed_content)


def copy_file(input_path, output_path):
    content = read_file(input_path)
    write_file(output_path, content)


def duplicate_contents(input_path, n):
    content = read_file(input_path)
    duplicated_content = content * n
    write_file(input_path, duplicated_content)


def replace_string(input_path, string, new_string):
    content = read_file(input_path)
    replaced_content = content.replace(string, new_string)
    write_file(input_path, replaced_content)


def main():
    if len(sys.argv) < MIN_NUM_ARGS:
        print("Usage: python3 file_manipulator.py command inputpath outputpath")
        sys.exit(1)

    command = sys.argv[1]
    input_path = sys.argv[2]
    validate_input_path(input_path)

    if command == "reverse":
        output_path = sys.argv[3]
        reverse_file_content(input_path, output_path)
    elif command == "copy":
        output_path = sys.argv[3]
        copy_file(input_path, output_path)
    elif command == "duplicate-contents":
        n = int(sys.argv[3])
        duplicate_contents(input_path, n)
    elif command == "replace-string":
        string, new_string = sys.argv[3], sys.argv[4]
        replace_string(input_path, string, new_string)
    else:
        print(f"Unknown command: {command}")
        print("Usage: python3 file_manipulator.py command inputpath outputpath")


if __name__ == "__main__":
    main()
