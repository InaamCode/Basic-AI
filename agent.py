import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load variables from your local .env file
load_dotenv()

def create_coding_agent():
    # Retrieve API key from environment (checks both standard and custom variable names)
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("Gemini_API")
    
    if not api_key:
        print("❌ Error: GEMINI_API_KEY environment variable is not set.")
        print("Please set GEMINI_API_KEY in your .env file or environment variables.")
        return

    # Initialize the Google GenAI Client with the retrieved key
    client = genai.Client(api_key=api_key)

    # System instruction guiding the model's persona and architecture role
    system_instruction = (
        "You are an expert AI Software Engineer and Technical Architect assistant. "
        "Your role is to help write, debug, refactor, and structure Python and software projects. "
        "When requested, generate complete, clean, documented, and modular code. "
        "When executing math or algorithmic validation, use the built-in code execution tool."
    )

    # Enable native code execution tool
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.2,  # Low temperature for precise code generation
        tools=[types.Tool(code_execution=types.ToolCodeExecution())]
    )

    # Create a persistent chat session using Gemini 3.6 Flash
    chat = client.chats.create(
        model="gemini-3.6-flash",
        config=config
    )

    print("=" * 60)
    print("🤖 AI Coding & Project Assistant Initialized")
    print("Type 'exit' or 'quit' to end the session.")
    print("=" * 60 + "\n")

    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting session. Happy coding!")
                break

            print("\n🤖 Assistant is thinking...\n")
            
            # Send message to the agent chat session
            response = chat.send_message(user_input)

            # Display agent response
            print("🤖 Agent:")
            print(response.text)

        except KeyboardInterrupt:
            print("\nSession interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\n❌ Error encountered: {e}")

if __name__ == "__main__":
    create_coding_agent()