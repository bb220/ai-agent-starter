import os
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from app.tools.balance_tool import get_user_balance

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

tools = [get_user_balance]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)
