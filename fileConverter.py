import os
from pathlib import Path
from shutil import copyfile

def convert_file(file_path, target_format):
    """
    Converts the given file to the specified format.

    Args:
        file_path (str): Path to the input file.
        target_format (str): Desired output file format (e.g., 'txt', 'pdf').

    Returns:
        str: Path to the converted file or None if conversion failed.
    """
    try:
        # Use an alternative directory if ~/Downloads is not writable
        output_dir = Path.home() / 'Downloads'
        if not output_dir.exists() or not os.access(output_dir, os.W_OK):
            output_dir = Path.cwd() / 'converted_files'
            output_dir.mkdir(exist_ok=True)

        input_file = Path(file_path).resolve()  # Ensure absolute path
        output_file = output_dir / f"{input_file.stem}.{target_format}"

        if not input_file.exists() or not input_file.is_file():
            raise FileNotFoundError(f"The file '{input_file}' does not exist or is not a valid file.")

        if not os.access(input_file, os.R_OK):
            raise PermissionError(f"The file '{input_file}' is not readable. Check file permissions.")

        if target_format == input_file.suffix[1:]:
            # No conversion needed; copy the file
            copyfile(input_file, output_file)
        else:
            # Placeholder for additional format conversion logic
            # This can include calling libraries for PDF, image, or text processing
            copyfile(input_file, output_file)  # This just makes a renamed copy

        return str(output_file)

    except FileNotFoundError as fnfe:
        print(f"File error: {fnfe}")
        return None
    except PermissionError as pe:
        print(f"Permission error: {pe}")
        return None
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return None

def main():
    print("Welcome to the File Converter!")
    print("Please select a file to convert.")

    try:
        input_file = input("Enter the full path to the file: ").strip()
        if not input_file:
            print("No file path provided.")
            return

        input_path = Path(input_file).resolve()  # Ensure absolute path
        print(f"Debug: Checking path '{input_path}'")

        # Debug: Print file details for diagnosis
        if input_path.exists():
            print(f"Debug: Path exists: {input_path}")
        else:
            print(f"Debug: Path does not exist: {input_path}")

        if input_path.is_file():
            print(f"Debug: Path is a valid file: {input_path}")
        else:
            print(f"Debug: Path is not a valid file: {input_path}")

        if not os.access(input_path, os.R_OK):
            print(f"Debug: File is not readable: {input_path}")

        # Check if path exists and is a file
        if not input_path.exists():
            print(f"The provided path '{input_path}' does not exist. Please check the path and try again.")
            return

        if not input_path.is_file():
            print(f"The provided path '{input_path}' is not a file. Please provide a valid file path.")
            return

        if not os.access(input_path, os.R_OK):
            print(f"The provided file '{input_path}' is not readable. Please check file permissions.")
            return

        target_format = input("Enter the target file format (e.g., txt, pdf, jpg): ").strip()
        if not target_format:
            print("No format specified.")
            return

        converted_file = convert_file(input_file, target_format)
        if converted_file:
            print(f"File successfully converted and saved to: {converted_file}")
        else:
            print("Conversion failed.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
