import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import datetime
from datetime import date


# Creating a chat bot named Charlie
chatbot = ChatBot('Charlie', storage_adapter='chatterbot.storage.SQLStorageAdapter',logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.5
        }
    ])


corpus_trainer = ChatterBotCorpusTrainer(chatbot)

# Training the chatbot using the English language corpus data
corpus_trainer.train('chatterbot.corpus.english')


def get_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    return f"It's {current_time}."


def get_current_date():
    current_date = date.today()
    return f"Today's date is {current_date}."


user_name = input("Charlie: Hi, I am your virtual assistant Charlie! What is your name?\nUser: ")
response = chatbot.get_response(f"My name is {user_name}.")
print(f"Charlie: {user_name} is such a lovely name! How are you doing today?")


trainer = ListTrainer(chatbot)
trainer.train([
    "Hi, I am your virtual assistant Charlie!",
    "Hi Charlie",
    "What's your name?",
    f"My name is {user_name}",
    f"{user_name} is such a lovely name! How are you doing today?",
    "I'm doing good",
    "That's good to hear",
    "What is your purpose?",
    "I'm here to assist you with information and tasks.",
    "What's the weather like today?",
    "I don't have real-time weather information. You can check a weather website or app for the latest updates.",
    "What time is it?",
    get_current_time(),
    "What is today's date?",
    get_current_date(),
    "What is 10 + 5?",
    "The result of 10 + 5 is 15.",
    "Tell me a joke.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Thank you.",
    "You're welcome.",
    "Goodbye",
    "Goodbye! If you have more questions, feel free to ask.",
])


conversation_history = []

while True:
    user_input = input(f"{user_name}: ")
    conversation_history.append(user_input)

    if user_input.lower() == 'bye':
        response = chatbot.get_response("Goodbye! If you have more questions, feel free to ask.")
        conversation_history.append(f"Charlie: {response}")
        print(f"Charlie: {response}")
        break

    response = chatbot.get_response(user_input)

    if user_input.lower() == "what time is it" or user_input.lower() == "what is the time":
        response = get_current_time()
    elif user_input.lower() == "what is today's date":
        response = get_current_date()

    conversation_history.append(f"Charlie: {response}")
    print(f"Charlie: {response}")
