import ollama

print("Starting...")

response = ollama.chat(
    model="llama3:latest",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)

print(response)