from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model="gemini-2.0-flash-live-001",  # Essential for live voice interaction since it supports both text and voice interaction
    name="ai_news_agent_simple",
    instruction="You are an AI News Assistant.",
)
