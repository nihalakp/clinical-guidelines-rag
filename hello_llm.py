import anthropic                                                    # loads the Anthropic Python SDK to interact with the Anthropic API
from dotenv import load_dotenv                                      # loads environment variables from a .env file

load_dotenv()                                                       # loads the API keys from the .env file into environment variables
client = anthropic.Anthropic()                                      # creates a client to interact with the Anthropic API

def ask(question: str) -> None:                                     # defines a function to ask a question to the model and stream the response
    """Stream a response from Claude."""                            # docstring for the ask function
    print(f"\nQuestion: {question}\n")                              # prints the question to the console
    print("Answer: ", end="", flush=True)                           # prints the question and prepares to print the answer without a newline, flushing the output buffer immediately

    with client.messages.stream(                                    # starts a streaming response from the model
        model="claude-sonnet-4-6",                                  #   specifies the model to use
        max_tokens=512,                                             #   specifies the maximum number of tokens to generate
        messages=[{"role": "user", "content": question}],           #   provides the input message to the model, indicating that it is from the user
        system="You are a clinical guidelines expert. Answer concisely and cite your reasoning."
    ) as stream:                                                    #   specifies a system prompt to guide the models behavior, indicating that it should act as a clinical guidelines expert and provide concise answers with cited reasoning
        for text in stream.text_stream:                             # iterates over the streamed text response from the model, printing each chunk of text as it is received
            print(text, end="", flush=False)                        # prints the streamed text without a newline and flushes the output buffer immediately to ensure that the response is displayed in real-time

    print("\n")

if __name__ == "__main__":
    question = input("Enter your question: ")                       # prompts the user to enter a question and stores it in the variable 'question'
    ask(question)                                                   # calls the ask function with the user's question to get and display the response from the model  