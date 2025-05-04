def write_to_console(text):
    """
    Outputs the given text to the console.

    Args:
        text (str): The text to print.
    """
    print(text)

def write_to_file_builtin(filename, text):
    """
    Writes the given text to a file using built-in Python functionality.

    Args:
        filename (str): The path to the file.
        text (str): The text to write.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
