from langchain.tools import tool

@tool
def get_user_balance(user_id: str) -> str:
    """Get a user's balance by ID."""
    return f"User {user_id} has a balance of $1,234.56."
