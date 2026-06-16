import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

def ask(question: str) -> None:
    """Stream a response from Claude."""
    print(f"\nQuestion: {question}\n")
    print("Answer: ", end="", flush=True)

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=512,
        messages=[{"role": "user", "content": question}],
        system="You are a clinical guidelines expert. Answer concisely and cite your reasoning."
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

    print("\n")

if __name__ == "__main__":
    ask("What is the typical criteria for inpatient hospital admission?")
