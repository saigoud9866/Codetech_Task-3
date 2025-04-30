# Codetech_Task-3
PROJECT ON PYTHON LEARNING

Overview
This project implements a simple rule-based chatbot with Natural Language Processing (NLP) capabilities using Python's NLTK library. The chatbot can understand user queries, match them to known patterns, and respond appropriately using cosine similarity for question matching.

Features
Natural Language Understanding: Uses NLTK for tokenization and lemmatization

Question Matching: Implements TF-IDF vectorization and cosine similarity

Conversational Flow: Handles greetings, questions, and exit commands

Knowledge Base: Contains predefined responses for common questions

Error Handling: Gracefully manages unexpected inputs and errors

Requirements
Python 3.6+

Required libraries:

bash
pip install nltk scikit-learn
Installation
Clone the repository:

bash
git clone https://github.com/yourusername/nlp-chatbot.git
cd nlp-chatbot
Install dependencies:

bash
pip install -r requirements.txt
Run the chatbot:

bash
python chatbot.py
How It Works
The chatbot initializes with:

Greeting patterns and responses

Exit commands

A knowledge base of question-answer pairs

When a user inputs text:

The text is preprocessed (tokenized and lemmatized)

TF-IDF vectors are created for similarity comparison

Cosine similarity finds the best matching question

The corresponding answer is returned

Special cases:

Greetings trigger random friendly responses

Exit commands end the conversation

Unknown queries get a default response

Customization
To extend the chatbot:

Add more question-answer pairs to knowledge_base

Expand greeting_inputs and greeting_responses

Add more exit commands to exit_commands

Improve the preprocessing in lemmatize_sentence()

Example Usage
python
bot = SimpleChatbot()
bot.chat()
Sample conversation:

Bot: Hello! I'm a simple chatbot...
You: hi
Bot: hello there!
You: what can you do?
Bot: I can answer simple questions...
You: quit
Bot: Goodbye!
