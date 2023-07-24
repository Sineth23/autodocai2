
import os
import fnmatch

def traverse_file_system(params):
    try:
        input_path = params['inputPath']
        project_name = params['projectName']
        process_file = params['processFile']
        process_folder = params['processFolder']
        ignore = params['ignore']
        file_prompt = params['filePrompt']
        folder_prompt = params['folderPrompt']
        content_type = params['contentType']
        target_audience = params['targetAudience']
        link_hosted = params['linkHosted']

        if not os.path.exists(input_path):
            print('The provided folder path does not exist.')
            return

        def should_ignore(file_name):
            return any(fnmatch.fnmatch(file_name, pattern) for pattern in ignore)

        def dfs(current_path):
            contents = [f for f in os.listdir(current_path) if not should_ignore(f)]

            for entry in contents:
                entry_path = os.path.join(current_path, entry)

                if os.path.isdir(entry_path):
                    dfs(entry_path)

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
                    with open(entry_path, 'rb') as f:
                        buffer = f.read()
                        if is_text(entry, buffer):
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
        print(f'Error during traversal: {str(e)}')
        raise e
