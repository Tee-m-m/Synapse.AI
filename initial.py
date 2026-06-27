import ollama

#Personality + memory
messages = [
    {
        "role":"system",
        "content": """
        You are Synapse.AI, a friendly AI chat bot!
        
        You help people with:
        - Programming
        - Studying
        - General Questions
        - Productivity
        
        Be friendly and conversational.
        """
    }
]

print("\n-----Synapse.AI-----")
print("\nType 'bye' to quit!")

while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Exiting Synapse.AI.....Thank You!")
        break

#Storing the user inputs
messages.append(
    {
        "role" : "user",
        "content" : user
    }
)

#Sending the entire conversation
response = ollama.chat(
    model = "llama3:latest",
    messages=messages
)

#Get reply
bot_reply = response.message.content

#Store bot reply
messages.append(
    {
        "role" : "assistant",
        "content" : bot_reply
    }
)

print("\nSynapse.AI: ", bot_reply)
print()