import streamlit as st
from pdfminer.high_level import extract_text
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import numpy as np
import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize the chatbot variables
raw_text = """[Your raw text here]"""
sentence_tokens = nltk.sent_tokenize(raw_text)
word_tokens = nltk.word_tokenize(raw_text)
lemmer = nltk.stem.WordNetLemmatizer()

# Text preprocessing functions
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

greet_inputs = ('hello', 'hi', 'whassup', 'namaste', 'kemchoo', 'how are you')
greet_responses = ('hi', 'hey there', 'i am fine', 'good', 'me too')

def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)

def response(user_response):
    robot_response = ' '
    TfidVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robot_response = robot_response + "I am sorry. Unable to understand. Please use more specific words in your prompt or remove any typing errors!"
        return robot_response
    else:
        robot_response = robot_response + sentence_tokens[idx]
        return robot_response

def text_to_pdf(text, output_file):
    c = canvas.Canvas(output_file, pagesize=letter)
    c.setFont("Helvetica", 12)
    lines = text.split('\n')
    y = 750
    for line in lines:
        c.drawString(50, y, line)
        y -= 15
    c.save()

# Streamlit app
st.title("NLP Chatbot")
st.write("Welcome to the NLP chatbot. Ask me anything!")

user_input = st.text_input("You: ", "")
if st.button("Send"):
    if user_input:
        if greet(user_input) is not None:
            response_text = greet(user_input)
        else:
            sentence_tokens.append(user_input)
            word_tokens.extend(nltk.word_tokenize(user_input))
            response_text = response(user_input)
            sentence_tokens.remove(user_input)
        st.write("Bot: " + response_text)
    else:
        st.write("Please enter a message to get a response.")

st.write("## Convert Text to PDF")
raw_text = st.text_area("Enter text to convert to PDF:", "")
output_file = "output.pdf"
if st.button("Convert to PDF"):
    if raw_text:
        text_to_pdf(raw_text, output_file)
        st.write("PDF created successfully!")
        with open(output_file, "rb") as pdf_file:
            st.download_button("Download PDF", data=pdf_file, file_name=output_file, mime="application/pdf")
    else:
        st.write("Please enter some text to convert to PDF.")