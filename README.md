# 🤖 CharlieBot – A Basic Chatbot

**CharlieBot** is a Python chatbot that demonstrates how to build a conversational agent using the ChatterBot library. It offers friendly greetings, remembers previous interactions, and adapts its responses based on context.

## 🎯 Project Objectives
- Introduce a beginner‑friendly chatbot framework.
- Demonstrate context awareness by remembering user interactions.
- Provide a foundation for more advanced conversational agents.

## 🧰 Features
- **Greeting & Farewell**: Welcomes users and ends conversations pleasantly.
- **Context Memory**: Recalls past inputs during the session for more coherent responses.
- **Dynamic Interaction**: Asks users questions to gather information and personalize its responses.
- **Custom Training Data**: Includes a training set of conversational phrases to handle common queries.

## 🧠 Methodology
- Built with the **ChatterBot** Python library using the **BestMatch** logic adapter.
- Trained on:
  - The built‑in English corpus.
  - A custom dataset found in `data/training_data.yml`.  You can modify or expand this to teach CharlieBot new responses.
- Conversations are logged in memory to maintain context during a session.

## 🗂 Project Structure
```bash
AIML-Project-1--Basic-Chatbot/
├── data/
│ └── training_data.yml # Custom training phrases
├── chatbot.py # Main script to run the bot
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

## 🛠 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nysajain/AIML-Project-1--Basic-Chatbot.git
   cd AIML-Project-1--Basic-Chatbot

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   
## 🚀 Usage

Run the chatbot from the command line:
```bash
python chatbot.py
```

CharlieBot will greet you and start asking questions. Try asking:
- “What can you do?”
- “Who created you?”
- “Tell me a joke.”

## 📊 Results / Evaluation
Since CharlieBot uses rule‑based matching, its quality depends on the training data. You can measure effectiveness by adding test phrases and checking for correct responses.

## 🧑‍💼 Author & Contributions
Developed by Nysa Jain as a learning project.
Contributions are welcome—open an issue or PR if you have ideas!
