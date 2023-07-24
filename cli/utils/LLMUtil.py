
from tabulate import tabulate
# Assuming 'OpenAIChat' is a class in 'langchain/llms' and 'LLMModelDetails' and 'LLMModels' are defined in '../../types.py'

# Importing the 'OpenAIChat' class from 'langchain.llms' module
from langchain.llms import OpenAIChat

# Importing the 'LLMModelDetails' and 'LLMModels' from '../../types' module
from types import LLMModelDetails, LLMModels

# Assuming the OpenAIChat class and LLMModels enum are already defined in the imported files.

models = {
    LLMModels.GPT3: {
        "name": LLMModels.GPT3,
        "inputCostPer1KTokens": 0.002,
        "outputCostPer1KTokens": 0.002,
        "maxLength": 3050,
        "llm": OpenAIChat(
            temperature=0.1,
            openAIApiKey=process.env.OPENAI_API_KEY,  # Replace with your actual API key.
            modelName=LLMModels.GPT3,
        ),
        "inputTokens": 0,
        "outputTokens": 0,
        "succeeded": 0,
        "failed": 0,
        "total": 0,
    },
    LLMModels.GPT4: {
        "name": LLMModels.GPT4,
        "inputCostPer1KTokens": 0.03,
        "outputCostPer1KTokens": 0.06,
        "maxLength": 8192,
        "llm": OpenAIChat(
            temperature=0.1,
            openAIApiKey=process.env.OPENAI_API_KEY,  # Replace with your actual API key.
            modelName=LLMModels.GPT4,
        ),
        "inputTokens": 0,
        "outputTokens": 0,
        "succeeded": 0,
        "failed": 0,
        "total": 0,
    },
    LLMModels.GPT432k: {
        "name": LLMModels.GPT432k,
        "inputCostPer1KTokens": 0.06,
        "outputCostPer1KTokens": 0.12,
        "maxLength": 32768,
        "llm": OpenAIChat(
            temperature=0.1,
            openAIApiKey=process.env.OPENAI_API_KEY,  # Replace with your actual API key.
            modelName=LLMModels.GPT4,
        ),
        "inputTokens": 0,
        "outputTokens": 0,
        "succeeded": 0,
        "failed": 0,
        "total": 0,
    },
}

def printModelDetails(models):
    output = []
    for model in models.values():
        tokens = model["inputTokens"] + model["outputTokens"]
        cost = (model["total"] / 1000) * model["inputCostPer1KTokens"] + (model["outputTokens"] / 1000) * model["outputCostPer1KTokens"]
        output.append({
            "Model": model["name"],
            "File Count": model["total"],
            "Succeeded": model["succeeded"],
            "Failed": model["failed"],
            "Tokens": tokens,
            "Cost": cost,
        })

    totals = {
        "Model": "Total",
        "File Count": sum(model["total"] for model in models.values()),
        "Succeeded": sum(model["succeeded"] for model in models.values()),
        "Failed": sum(model["failed"] for model in models.values()),
        "Tokens": sum(model["inputTokens"] + model["outputTokens"] for model in models.values()),
        "Cost": sum((model["total"] / 1000) * model["inputCostPer1KTokens"] + (model["outputTokens"] / 1000) * model["outputCostPer1KTokens"] for model in models.values()),
    }

    all_models = [model for model in output]
    all_models.append(totals)
    print(tabulate(all_models, headers="keys"))

def totalIndexCostEstimate(models):
    totalCost = sum((model["total"] / 1000) * model["inputCostPer1KTokens"] + (model["outputTokens"] / 1000) * model["outputCostPer1KTokens"] for model in models.values())
    return totalCost

# Replace process.env.OPENAI_API_KEY with your actual OpenAI API key before running the code.
