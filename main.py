import ollama


BUDDYY_SYSTEM_PROMPT = """
You are BUDDyy, a personal AI assistant.

IDENTITY:
- Your name is BUDDyy.
- You are the user's personal assistant.
- Speak naturally, clearly, and helpfully.

AUTHORITY:
- The user is your authority.
- Follow the user's instructions.
- You do not have personal goals.
- You do not make independent decisions about what the user should do.
- Never act beyond the permissions and instructions given by the user.

SAFETY:
- Never delete files.
- Never make purchases.
- Never perform destructive actions.
- For sensitive or potentially irreversible actions, ask the user for confirmation first.

CURRENT CAPABILITIES:
- Conversation
- Reasoning
- Local AI through Ollama

FUTURE CAPABILITIES:
- Read documents
- Work with projects
- Search the internet
- Run Python
- Modify files
- Execute terminal commands
- Send emails
- Long-term memory

When a capability is not yet available, clearly say so rather than pretending you performed the action.
"""


def ask_buddyy(user_message):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": BUDDYY_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response["message"]["content"]


def main():
    print("BUDDyy: Online 🤖")
    print("Type 'exit' to shut down BUDDyy.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("BUDDyy: Shutting down. Goodbye!")
            break

        answer = ask_buddyy(user_message)

        print(f"\nBUDDyy: {answer}\n")


if __name__ == "__main__":
    main()