# 🤖 AI Agent Starter

## Overview

A minimal template for building **AI agents** using [LangChain](https://github.com/langchain-ai/langchain).

This agent uses a single OpenAI model and a customizable set of tools to answer user queries.


## Project Structure

- **app/**: Contains the main application scripts and tools.
  - **agent.py**: Core functionalities for the AI agent.
  - **main.py**: Entry point for running the application.
  - **tools/**: Directory containing utility scripts.
    - **balance_tool.py**: Tool for managing user balance functionalities.
- **.env**: Environment variables configuration file.
- **requirements.txt**: Lists all Python dependencies required for the project.

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment tool (e.g., `venv`)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-agent-starter
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source .venv/bin/activate
     ```
5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

- Run the main application:
  ```bash
  python app/main.py
  ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.
