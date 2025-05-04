from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import write_to_console, write_to_file_builtin


def main():
    console_text = read_from_console()
    write_to_console(console_text)
    write_to_file_builtin("console_output.txt", console_text)

    file_text = read_from_file_builtin("file_input.txt")
    write_to_console(f"\nFile content:\n{file_text}")
    write_to_file_builtin("file_output.txt", file_text)

    pandas_text = read_from_file_pandas("csv_test.csv")
    write_to_console(f"\nCSV file content:\n{pandas_text}")
    write_to_file_builtin("pandas_output.txt", pandas_text)


if __name__ == '__main__':
    main()