import datetime
import os


def save_to_file(xml_string: str, file_name: str = None, folder: str = None):
    if not folder:
        folder = os.getcwd()  # Get the current working directory
    if not file_name:
        file_name = f'Dump{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.xml'

    file_path = os.path.join(folder, file_name)

    try:
        with open(file_path, 'w') as f:
            f.write(xml_string)
        print(f'File saved to {file_path}')
    except Exception as e:
        print(f'Error while saving file: {e}')

    return file_path
