import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

def send_message(prompt: str) -> str:
    """Send a message to Claude using the official API

    Args:
        prompt (str): The message to send to Claude

    Returns:
        str: Claude's response
    """
    client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text

def main():
    # Example usage
    prompt = "What's the current date?"
    response = send_message(prompt)
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()