import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

class SimpleChatbot:
    def __init__(self):
        self.greeting_inputs = ("hello", "hi", "greetings", "sup", "what's up", "hey")
        self.greeting_responses = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
        self.exit_commands = ["quit", "pause", "exit", "goodbye", "bye", "later"]
        
        # Enhanced knowledge base
        self.knowledge_base = {
            "what is your name": "I'm a simple chatbot. You can call me ChatBot!",
            "who created you": "I was created by SAI TEJA using Python and NLTK.",
            "how are you": "I'm just a program, so I'm always functioning perfectly!",
            "what can you do": "I can answer simple questions and have basic conversations.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "what is nltk": "NLTK is the Natural Language Toolkit, a Python library for working with human language data.",
            "how does this work": "I use NLP techniques like tokenization and cosine similarity to understand your questions.",
            "default": "I'm sorry, I don't understand that. Could you rephrase or ask something else?"
        }
        
        # Prepare the knowledge base for similarity comparison
        self.sent_tokens = list(self.knowledge_base.keys()) + list(self.greeting_inputs)
        self.lemmer = nltk.stem.WordNetLemmatizer()
        
        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(tokenizer=self.lemmatize_sentence, stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.sent_tokens)
    
    def lemmatize_sentence(self, sentence):
        return [self.lemmer.lemmatize(token.lower().strip()) for token in nltk.word_tokenize(sentence)]
    
    def respond(self, user_input):
        if user_input.lower() in self.exit_commands:
            return "Goodbye! Have a nice day."
            
        if user_input.lower() in [g.lower() for g in self.greeting_inputs]:
            return random.choice(self.greeting_responses)
        
        # Add user input to the sentence tokens temporarily for comparison
        all_sentences = self.sent_tokens + [user_input]
        tfidf_matrix = self.vectorizer.transform(all_sentences)
        
        # Calculate cosine similarity
        vals = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        
        if req_tfidf == 0:
            return self.knowledge_base["default"]
        else:
            best_match_sentence = all_sentences[idx]
            return self.knowledge_base.get(best_match_sentence, self.knowledge_base["default"])
    
    def chat(self):
        print("Bot: Hello! I'm a simple chatbot. You can ask me questions or say hello. Type 'quit' to exit.")
        print("Bot: Try asking things like: What is your name? Who created you? Tell me a joke.")
        
        while True:
            try:
                user_input = input("You: ")
                if not user_input.strip():
                    print("Bot: Please type something...")
                    continue
                    
                response = self.respond(user_input)
                print("Bot:", response)
                
                if user_input.lower() in self.exit_commands:
                    break
                    
            except KeyboardInterrupt:
                print("\nBot: Goodbye!")
                break
            except Exception as e:
                print(f"Bot: Sorry, I encountered an error. {str(e)}")
                continue

# Run the chatbot
if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()