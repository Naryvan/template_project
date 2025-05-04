import pandas as pd

def read_from_console():
    """
    Reads input text from the console.

    Returns:
        str: Text entered by the user.
    """
    return input()

def read_from_file_builtin(filename):
    """
    Reads the entire content of a file using built-in Python functionality.

    Args:
        filename (str): The path to the file.

    Returns:
        str: The content of the file as a string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def read_from_file_pandas(filename):
    """
    Reads a CSV file using pandas and returns a DataFrame.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        str: The content of the file as a string.
    """
    return pd.read_csv(filename).to_string(index=False)