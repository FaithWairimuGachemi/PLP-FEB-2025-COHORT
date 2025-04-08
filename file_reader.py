def read_and_process_file():
    """
    Prompts user for filename and handles file reading errors.
    Returns file content if successful, None otherwise.
    """
    while True:
        try:
            filename = input("Enter filename to read: ")
            with open(filename, 'r') as file:
                content = file.read()
                return content
                
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please try again.")
        except PermissionError:
            print(f"Error: No permission to read '{filename}'. Please try another file.")
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory. Please enter a file path.")
        except UnicodeDecodeError:
            print(f"Error: Could not decode '{filename}'. Try a different file encoding.")
        except Exception as e:
            print(f"Unexpected error reading file: {e}")
            
        retry = input("Try another file? (y/n): ")
        if retry.lower() != 'y':
            return None

def write_processed_file(content, output_path):
    """Writes processed content to output file with error handling"""
    try:
        with open(output_path, 'w') as file:
            file.write(content.upper())  # Example processing
        print(f"Successfully wrote to {output_path}")
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False

if __name__ == "__main__":
    print("File Reader with Error Handling")
    content = read_and_process_file()
    
    if content:
        output_file = input("Enter output file path: ")
        write_processed_file(content, output_file)
