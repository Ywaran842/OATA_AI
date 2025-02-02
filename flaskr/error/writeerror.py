import os
from datetime import datetime

def write_error_to_file(errormeassage, error_type='None'):
    # Ensure the 'error' directory exists
    error_directory = os.path.join('flaskr', 'error')
    if not os.path.exists(error_directory):
        os.makedirs(error_directory)

    # Construct the file path
    file_path = os.path.join(error_directory, f'{error_type}.error')

    # Format the error message with a timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    formatted_error = f'{timestamp} - {errormeassage}\n'

    try:
        # Open the file in append mode and write the error
        with open(file_path, 'a') as file:
            file.write(formatted_error)
    except Exception as e:
        print(f'Error writing to file: {e}')
