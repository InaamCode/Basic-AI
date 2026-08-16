import os
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from .env
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is not set. Please add it to your .env file."
    )

# Create OpenAI client
client = OpenAI(api_key=api_key)


def ask_agent(user_input):
    """Send user input to the AI model and return the response."""

    response = client.responses.create(
        model="gpt-5.6",
        input=user_input
    )

    return response.output_text


def main():
    print("=" * 50)
    print("             BASIC AI AGENT")
    print("=" * 50)
    print("Type 'exit' to close the agent.")
    print()

    while True:
        user_input = input("You: ").strip()

        # Exit command
        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        # Empty input
        if not user_input:
            print("Agent: Please enter a question.")
            continue

        # Ask AI
        try:
            answer = ask_agent(user_input)
            print("Agent:", answer)
            print()

        except Exception as error:
            print("Agent Error:", error)


if __name__ == "__main__":
    main()
