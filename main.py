from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import datetime

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie', storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, but I do not understand.',
        'maximum_similarity_threshold': 0.9
    }
])

trainer = ListTrainer(chatbot)

# Train with more diverse data
trainer.train([
    "Hi, I am your virtual assistant Charlie!",
    "Hi Charlie",
    "How are you?",
    "I'm just a computer program, but thanks for asking!",
    "What's your name?",
    "I am Charlie, your virtual assistant.",
    "What is your purpose?",
    "I'm here to assist you with information and tasks.",
    "What's the weather like today?",
    "I don't have real-time weather information. You can check a weather website or app for the latest updates.",
    "What time is it?",
    "I don't have the current time, please check your watch",
    "What is 10 + 5?",
    "The result of 10 + 5 is 15.",
    "Tell me a joke.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Goodbye",
    "Goodbye! If you have more questions, feel free to ask.",
])

# Use dynamic user interaction
user_name = input("Charlie: Hi, I am your virtual assistant Charlie! What is your name?\nUser: ")
response = chatbot.get_response(f"My name is {user_name}.")
print(f"Charlie: {user_name} is such a lovely name! How are you doing today?")

conversation = []  # Maintain a list to store the conversation

while True:
    user_input = input(f"{user_name}: ")
    conversation.append(f"{user_name}: {user_input}")

    if user_input.lower() == 'bye':
        response = chatbot.get_response("Goodbye! If you have more questions, feel free to ask.")
        conversation.append(f"Charlie: {response}")
        print(f"Charlie: {response}")
        break
    else:
        response = chatbot.get_response(user_input)
        conversation.append(f"Charlie: {response}")
        print(f"Charlie: {response}")
