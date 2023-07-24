
import os
import subprocess
import shutil
from typing import Dict, List
from processRepository import process_repository  # Assuming processRepository is implemented in a Python module
from LLMUtil import print_model_details, total_index_cost_estimate  # Assuming LLMUtil is implemented in a Python module
import chalk  # Assuming you have a Python library that provides colored terminal output

def estimate(config: Dict) -> None:
    output_folder = os.path.join(config['output'], 'docs', 'json/')

    # Dry run of the process_repository command to get the estimated price for indexing the repo
    print('Estimating cost...')
    run_details = process_repository(config, dry_run=True)

    # Print Results
    print_model_details(list(run_details.values()))
    total = total_index_cost_estimate(list(run_details.values()))
    print(
        chalk.redBright(
            f"Cost estimate to process this repository: ${total:.2f}\nThis is just an estimate. Actual cost may vary.\nIt is recommended that you set a limit in your OpenAI account to prevent unexpected charges."
        )
    )

# Example usage:
#config = {
 #   "name": "my_repo",
  #  "repositoryUrl": "https://github.com/your-username/your-repo.git",
   # "root": "path/to/your/repo",
    #"output": "path/to/output/folder",
    #"llms": ["gpt-3.5-turbo", "gpt-4", "gpt-4-32k"],
    #"ignore": ["node_modules", ".git"],
    #"filePrompt": "What is the content of this file?",
    #"folderPrompt": "Describe the folder:",
    #"chatPrompt": "Describe the chat:",
    #"contentType": "documentation",
    #"targetAudience": "developers",
    #"linkHosted": True
#}

#estimate(config)
