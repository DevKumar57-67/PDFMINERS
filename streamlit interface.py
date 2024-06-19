import streamlit as st

# Streamlit app
st.title("NLP Chatbot")
st.write("Welcome to  PDFMinez.Make your text into pdf with just one click!")


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
        
#Streamlit frontend interface of the chatbot 
                                      