import os
import asyncio
from agent_framework.azure import AzureOpenAIResponsesClient
from code.utils.file_util import FileUtil
from code.utils.context_provider import ContextProvider
from dotenv import load_dotenv


def get_env_variable(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Missing required environment variable: {name}")
    return value

async def run_agent():
    """
    Loads prompts, prints them, and runs the agent with the user prompt.
    """
    # Load environment variables from .env file at project root
    load_dotenv()

    # Print banner
    print("""
========================================
        Context Agent Showcase
========================================
            """)

    # Read and print prompts
    system_prompt = FileUtil.read_file("/prompt/vanilla-agent-system-prompt.md")
    user_prompt = FileUtil.read_file("/prompt/user-prompt.md")
    print("System Prompt:\n" + (system_prompt or "[Empty]") + "\n" + "-"*40)
    print("User Prompt:\n" + (user_prompt or "[Empty]") + "\n" + "-"*40)


    # Load Azure OpenAI configuration from environment variables
    endpoint = get_env_variable("azure_endpoint")
    api_key = get_env_variable("azure_apikey")
    deployment_name = get_env_variable("azure_deployment")
    api_version = get_env_variable("azure_version")

    agent = AzureOpenAIResponsesClient(
        endpoint=endpoint,
        deployment_name=deployment_name,
        api_version=api_version,
        api_key=api_key
    ).create_agent(
        name="spring-coder",
        instructions=system_prompt,
        context_providers=[ ContextProvider("/context/springboot-knowledge.md")],
    )

    # Run a sample query and print the result
    print("\nAgent Response:\n" + "="*40)
    response = await agent.run(user_prompt or "")
    print(response)

if __name__ == "__main__":
    asyncio.run(run_agent())