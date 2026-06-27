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
    try:
        print("\nSnappie: ", end='', flush=True)

        bot_reply = ""

        for chunk in ollama.chat(
            model="llama3.2:1b",
            messages=messages,
            stream=True
        ):
            word = chunk['message']['content']
            print(word, end='', flush=True)
            bot_reply+=word
            
        print("\n")


        #Store bot reply
        messages.append(
            {
                "role" : "assistant",
                "content" : bot_reply
            }
        )

    except Exception as e:
        print("Error:", e)