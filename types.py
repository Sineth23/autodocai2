
from typing import List

class OpenAIChat:
    pass

class AutodocUserConfig:
    def __init__(self, llms: List[str]):
        self.llms = llms

class AutodocRepoConfig:
    def __init__(self, name: str, repositoryUrl: str, root: str, output: str, llms: List[str], 
                 ignore: List[str], filePrompt: str, folderPrompt: str, chatPrompt: str, 
                 contentType: str, targetAudience: str, linkHosted: bool):
        self.name = name
        self.repositoryUrl = repositoryUrl
        self.root = root
        self.output = output
        self.llms = llms
        self.ignore = ignore
        self.filePrompt = filePrompt
        self.folderPrompt = folderPrompt
        self.chatPrompt = chatPrompt
        self.contentType = contentType
        self.targetAudience = targetAudience
        self.linkHosted = linkHosted

class FileSummary:
    def __init__(self, fileName: str, filePath: str, url: str, summary: str, questions: str, checksum: str):
        self.fileName = fileName
        self.filePath = filePath
        self.url = url
        self.summary = summary
        self.questions = questions
        self.checksum = checksum

class FolderSummary:
    def __init__(self, folderName: str, folderPath: str, url: str, files: List[FileSummary], 
                 folders: List['FolderSummary'], summary: str, questions: str, checksum: str):
        self.folderName = folderName
        self.folderPath = folderPath
        self.url = url
        self.files = files
        self.folders = folders
        self.summary = summary
        self.questions = questions
        self.checksum = checksum

class LLMModelDetails:
    def __init__(self, name: str, inputCostPer1KTokens: float, outputCostPer1KTokens: float, 
                 maxLength: int, llm: OpenAIChat, inputTokens: int, outputTokens: int, 
                 succeeded: int, failed: int, total: int):
        self.name = name
        self.inputCostPer1KTokens = inputCostPer1KTokens
        self.outputCostPer1KTokens = outputCostPer1KTokens
        self.maxLength = maxLength
        self.llm = llm
        self.inputTokens = inputTokens
        self.outputTokens = outputTokens
        self.succeeded = succeeded
        self.failed = failed
        self.total = total
