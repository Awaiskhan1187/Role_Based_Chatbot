content = {
    "hello": "hey there, how can i help you today?",
    "hi": "Hello! What can I do for you?",
    "How are you?": "I'm just a bot, but I'm doing great! How about you?",
    "your name": "I am ChatBot, your friendly AI assistant.",
    "help": "I can chat about greeting, my name , more!",
    "bye": "Goodbye! Have a great day!",
}
print("ChatBot: Hello! I am ChatBot, your friendly AI assistant. Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    Prompt = user_input.lower().strip()
    if Prompt == "exit":
        response = content.get("bye")
        print("ChatBot:", response)
        break

    response = content.get(user_input, "I'm sorry, I don't understand that. Can you please rephrase?")
    print("ChatBot:", response)