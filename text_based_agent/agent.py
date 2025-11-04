from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model="gemini-2.5-flash",  # model supports text generation
    name="newsMan",
    instruction="You are an AI News Assistant.",
    tools=[google_search],  # external tool
)
