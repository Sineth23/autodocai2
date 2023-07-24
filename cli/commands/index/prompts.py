
from ../../../types import FileSummary, FolderSummary

from dataclasses import dataclass
from typing import List

def create_code_file_summary(filePath: str, projectName: str, fileContents: str, contentType: str, filePrompt: str) -> str:
    return f"""
    You are acting as a {contentType} documentation expert for a project called {projectName}.
    Below is the {contentType} from a file located at `{filePath}`. 
    {filePrompt}
    Do not say "this file is a part of the {projectName} project".

    {contentType}:
    {fileContents}

    Response:
    """

def create_code_questions(filePath: str, projectName: str, fileContents: str, contentType: str, targetAudience: str) -> str:
    return f"""
    You are acting as a {contentType} documentation expert for a project called {projectName}.
    Below is the {contentType} from a file located at `{filePath}`. 
    What are 3 questions that a {targetAudience} might have about this {contentType}? 
    Answer each question in 1-2 sentences. Output should be in markdown format.

    {contentType}:
    {fileContents}

    Questions and Answers:
    """

def folder_summary_prompt(folderPath: str, projectName: str, files: List[FileSummary], folders: List[FolderSummary],
                         contentType: str, folderPrompt: str) -> str:
    return f"""
    You are acting as a {contentType} documentation expert for a project called {projectName}.
    You are currently documenting the folder located at `{folderPath}`. 
    
    Below is a list of the files in this folder and a summary of the contents of each file:

    {"".join([f"Name: {file.fileName}\nSummary: {file.summary}\n\n" for file in files])}

    And here is a list of the subfolders in this folder and a summary of the contents of each subfolder:

    {"".join([f"Name: {folder.folderName}\nSummary: {folder.summary}\n\n" for folder in folders])}

    {folderPrompt}
    Do not say "this file is a part of the {projectName} project".
    Do not just list the files and folders.

    Response:
    """
