from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from cleaner import clean_corpus
import pickle
import os
CORPUS_FILE = open("chat.txt",encoding='UTF-8').read()

chatbot = ChatBot("Chatbot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)

chatbot = ChatBot("ChatBot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

with open('my_trained_model.pkl', 'wb') as f:
    pickle.dump(cleaned_corpus, f)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")