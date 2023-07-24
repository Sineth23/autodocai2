import os
import fnmatch
from typing import Callable, Optional
from typing_extensions import TypedDict
from types import TraverseFileSystemParams 




def traverse_file_system(params: TraverseFileSystemParams) -> None:
    try:
        input_path = params['inputPath']
        project_name = params['projectName']
        process_file = params.get('processFile')
        process_folder = params.get('processFolder')
        ignore = params['ignore']
        file_prompt = params['filePrompt']
        folder_prompt = params['folderPrompt']
        content_type = params['contentType']
        target_audience = params['targetAudience']
        link_hosted = params['linkHosted']

        try:
            os.access(input_path, os.R_OK)
        except FileNotFoundError:
            print('The provided folder path does not exist.')
            return

        def should_ignore(file_name: str) -> bool:
            return any(fnmatch.fnmatch(file_name, pattern) for pattern in ignore)

        def dfs(current_path: str) -> None:
            contents = [entry for entry in os.listdir(current_path) if not should_ignore(entry)]

            for entry in contents:
                entry_path = os.path.join(current_path, entry)
                if os.path.isdir(entry_path):
                    dfs(entry_path)
                    if process_folder:
                        process_folder({
                            'inputPath': input_path,
                            'folderName': entry,
                            'folderPath': entry_path,
                            'projectName': project_name,
                            'shouldIgnore': should_ignore,
                            'folderPrompt': folder_prompt,
                            'contentType': content_type,
                            'targetAudience': target_audience,
                            'linkHosted': link_hosted,
                        })
                elif os.path.isfile(entry_path):
                    with open(entry_path, 'rb') as file:
                        if is_text(entry, file.read()):
                            if process_file:
                                process_file({
                                    'fileName': entry,
                                    'filePath': entry_path,
                                    'projectName': project_name,
                                    'filePrompt': file_prompt,
                                    'contentType': content_type,
                                    'targetAudience': target_audience,
                                    'linkHosted': link_hosted,
                                })

        dfs(input_path)
    except Exception as e:
        print(f'Error during traversal: {e}')
        raise

# Replace is_text function with your actual implementation for checking if a file is a text file.
