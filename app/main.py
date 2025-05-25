import os
from dotenv import load_dotenv
from app.agent import agent


load_dotenv()

def main():
    print("\n✨ Welcome to the AI Agent ✨")
    print("Type \"q\" to quit.\n")
    while True:
        prompt = input("\nAsk a question: ")
        if prompt.lower() in ["q",]:
            break
        response =agent.run(prompt)
        print("🤖 Agent:", response)

if __name__ == "__main__":
    main()