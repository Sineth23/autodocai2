from dataclasses import dataclass
from typing import List

@dataclass
class OpenAIChat:
    # Your implementation of the OpenAIChat class here
    pass

@dataclass
class AutodocUserConfig:
    llms: List[str]

@dataclass
class AutodocRepoConfig:
    name: str
    repositoryUrl: str
    root: str
    output: str
    llms: List[str]
    ignore: List[str]
    filePrompt: str
    folderPrompt: str
    chatPrompt: str
    contentType: str
    targetAudience: str
    linkHosted: bool

@dataclass
class FileSummary:
    fileName: str
    filePath: str
    url: str
    summary: str
    questions: str
    checksum: str

@dataclass
class ProcessFileParams:
    fileName: str
    filePath: str
    projectName: str
    contentType: str
    filePrompt: str
    targetAudience: str
    linkHosted: bool

@dataclass
class FolderSummary:
    folderName: str
    folderPath: str
    url: str
    files: List[FileSummary]
    folders: List['FolderSummary']
    summary: str
    questions: str
    checksum: str

@dataclass
class ProcessFolderParams:
    inputPath: str
    folderName: str
    folderPath: str
    projectName: str
    contentType: str
    folderPrompt: str
    targetAudience: str
    linkHosted: bool
    shouldIgnore: callable

@dataclass
class TraverseFileSystemParams:
    inputPath: str
    projectName: str
    processFile: callable = None
    processFolder: callable = None
    ignore: List[str]
    filePrompt: str
    folderPrompt: str
    contentType: str
    targetAudience: str
    linkHosted: bool

class LLMModels:
    GPT3 = 'gpt-3.5-turbo'
    GPT4 = 'gpt-4'
    GPT432k = 'gpt-4-32k'

@dataclass
class LLMModelDetails:
    name: str
    inputCostPer1KTokens: float
    outputCostPer1KTokens: float
    maxLength: int
    llm: OpenAIChat
    inputTokens: int
    outputTokens: int
    succeeded: int
    failed: int
    total: int
