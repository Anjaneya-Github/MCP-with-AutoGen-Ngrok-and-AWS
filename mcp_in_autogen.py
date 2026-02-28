from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams
import os


async def main(main_task):

    params = StdioServerParams(
        command="uvx",
        args=["mcp-server-time", "--local-timezone=America/New_York"],
        startup_timeout=20
    )

    model = OpenAIChatCompletionClient(
        model="gpt-4",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.2,
    )

    async with McpWorkbench(server_params=params) as workbench:

        agent = AssistantAgent(
            name="Agent",
            system_message="You are a helpful assistant",
            model_client=model,
            workbench=workbench,
            reflect_on_tool_use=True
        )

        async for message in agent.run_stream(task=main_task):
            print("-" * 100)
            print(message)
            print("-" * 100)


if __name__ == "__main__":
    main_task = "Get time in London"
    asyncio.run(main(main_task))