!pip install reportlab
!pip install pdfminer.six



output_file = "output.pdf"
text_to_pdf(raw_text, output_file)





from pdfminer.high_level import extract_text
text=extract_text('output.pdf')
print(repr(text))
print(text)


# Function to convert text to vector
def text_to_vector(text):
    # Simulated method for converting text to vector
    return np.random.rand(1, 4)  # Replace with your actual method

# Function to get the intent based on input text
def get_intent(input_text):
    input_vector = text_to_vector(input_text)
    best_similarity = -1
    best_intent = None
    for intent, vector in vectors.items():
        similarity = cosine_similarity(input_vector, vector)[0][0]
        if similarity > best_similarity:
            best_similarity = similarity
            best_intent = intent
    return best_intent

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import numpy as np
import nltk
import random
import string

def text_to_pdf(text, output_file):
    # Create a canvas with letter size
    c = canvas.Canvas(output_file, pagesize=letter)

    # Set up the font and size
    c.setFont("Helvetica", 12)

    # Split text into lines and write to the canvas
    lines = text.split('\n')
    y = 750  # Starting y position
    for line in lines:
        c.drawString(50, y, line)
        y -= 15  # Adjust vertical position for the next line

    # Save the canvas as a PDF file
    c.save()

# Example usage:
raw_text = """

Sure, here's a classic one:

[Image of a teacher writing on the board with a caption that reads:]
"When the teacher erases the board but you weren't done copying the notes."

[Image of a student with a panicked expression trying to write down the notes before they disappear.]
Here you go:

[Image of a cricket player swinging and missing a ball with a caption that reads:]
"Me trying to hit deadlines on Mondays."

[Image of a cricket umpire signaling "out" with a caption that reads:]
"When your alarm goes off and you realize it's Monday morning."
How about this one:

[Image of a singer passionately belting out a note with a caption that reads:]
"When you're singing in the shower and suddenly remember you have an audience of shampoo bottles."

Here's a stand-up comedian meme for you:[Image of a stand-up comedian on stage with a microphone and a caption that reads:] "When you tell a joke to a small group and they all laugh, but then you try it with a larger crowd and it's just crickets."

How about this one:

[Image of a stand-up comedian on stage with a microphone and a caption that reads:]
"When you're a stand-up comedian telling political jokes and you see someone in the audience checking their phone for the latest news to fact-check you."
Here's a meme text on elections:

[Image of a person looking at a ballot paper with a puzzled expression and a caption that reads:]
"When you're trying to decide between the lesser of two evils."
Here you go:

[Image of a scientist looking through a microscope with a caption that reads:]
"When you're trying to find your way through life but end up in the lab instead."
How about this:

[Image of a person looking surprised with wide eyes and a caption that reads:]
"Gajab bejti hai... jab teacher achanak class mein aa jaaye aur tumne homework nahi kiya ho!"
Here's a meme text for you:

[Image of a person looking exasperated with a caption that reads:]
"Saans to lene de be... Assignment ka deadline abhi hai!"

Here's a meme text for you:

[Image of a person pointing with a serious expression and a caption that reads:]
"Dekh raha hai binod... jab bhi koi random comment section mein dikhe!"

Here you go:

[Image of a person with a shocked expression and a caption that reads:]
"Ye gaya 7 crore sidhe aapke bank account me... Phir alarm clock ne jagaya!"

Here you go:

[Image of a confident person with arms crossed and a caption that reads:]
"Jalwa hai hamara yahan... jab chai ki pyali aati hai!"

Here's one for you:

[Image of a determined person with books and papers around them and a caption that reads:]
"Abe padhai likhai karo, IAS bano... Tumhara future bhi toh trending hona chahiye!"
Sure, here it is:

[Image of a disappointed person with a caption that reads:]
"Beta tumse na ho payega... jab tumhe kisi ne 'Sunday ko bhi work from home ' bola."
Here's a meme text for you:

[Image of a person looking confident with a plan and a caption that reads:]
"Mast plan hai... jab tak reality check nahi aati."


Here's a meme text for you:

[Image of a person with a mischievous expression and a caption that reads:]
"Aag laga di, aag laga di... jab friend ne 'sirf ek episode dekhenge' kaha tha!"

Here you go:

[Image of a person looking perplexed with a caption that reads:]
"Is sajjan ko kya takleef hai... jab samajh nahi aata kuch samajhne ko milta hi nahi!"

Here's a meme text for you:

[Image of a person looking amazed with a caption that reads:]
"O ma go true love... jab wifi ke signals bhi aane lagte hain!"

Here's a meme text for you:

[Image of a person looking puzzled with a caption that reads:]
"Bhai kya kar raha hai tu... jab dost WhatsApp par 'typing...' dikha raha hai par message nahi bhej raha!"
Here's a meme text for you:

[Image of a person looking frustrated with a caption that reads:]
"Ye sab doglapan hai... jab dost restaurant me 'sirf ek bite le lunga' bolte hain, phir pura plate kha jate hain!"

Here's a meme text for you:

[Image of a person looking exhausted with a caption that reads:]
"Saala ye dukh kahe nahi khatam hota re... jab alarm lagaane ke baad bhi neend nahi aati!"

Here's a meme text for you:

[Image of a person looking dizzy with a caption that reads:]
"Arey mujhe chakkar aane lage hain... jab Sunday night ko hi Monday ka blues shuru ho jata hai!"
Here's a meme text for you:

[Image of a person looking determined with a caption that reads:]
"Paisa hi paisa hoga... jab salary aane wali ho!"
Here's a meme text for you:

[Image of a person looking impressed with a caption that reads:]
"Ye badiya tha guru... jab chai ke saath biscuit milta hai!"

Here's a meme text for you:

[Image of a person looking understanding with a caption that reads:]
"Pyaari samaj gayi... jab dost ne chupke se 'let's order pizza' bola."

Here's a meme text for you:

[Image of a person looking satisfied with a caption that reads:]
"Shuru majboori me kiye the, lekin ab maja araha hai... jab Sunday ko bhi office ka kaam mukammal ho jata hai!"
Here's a meme text for you:

[Image of a person looking confident with a caption that reads:]
"Bilkul risk nahi lene ka... jab subah late uthne par bhi traffic me phasna nahi hota!"

Here you go:

[Image of a person looking impressed with a caption that reads:]
"Shabhash beta... jab dost memes ki perfect timing samajh jaaye!"

Here's a meme text for you:

[Image of a person looking exasperated with a caption that reads:]
"Ek chota sa kaam tha... par phir usne 'just one more episode' bol diya!"

Here's a meme text for you:

[Image of a person looking secretive with a caption that reads:]
"Matter internal hai... jab dost kisi personal baat pe sawaal kare."

Here's a meme text for you:

[Image of a person looking innocent with a caption that reads:]
"Bade sanskaari ho beta... jab parents ke samne hi phone ka wallpaper change karte ho!"

Here's a meme text for you:

[Image of a person looking confident with a caption that reads:]
"Hum bhi pehle gaye the, tum bhi pehle jaoge... jab ek ladki do best friends ke sath two timing karti hain!"

Here's a meme text for you:

[Image of a person looking concerned with a caption that reads:]
"O chacha, rest karlo varna rest in peace ho jaoge... jab dost subah ke 5 baje tak gaming kar rahe hain!"

Here's a meme text for you:

[Image of a person looking frustrated with a caption that reads:]
"Har baar garam karke thanda hi chhod dete hain... jab chai ke saath biscuits khaane ki planning kar rahe ho aur fridge me kuch bacha hi nahi!"

Here's a meme text for you:

[Image of a person looking resigned with a caption that reads:]
"Aur game ek naya niyam add kar rahe hain... jab dost rules change karte hain aur tum abhi tak purane rules samaj nahi pa rahe ho!"

Here's a meme text for you:

[Image of a person looking doubtful with a caption that reads:]
"Wo to nahi ho payega... jab dost PUBG me chicken dinner expect karte hain par pehle hi zone me mare jaate hain!"

Here's a meme text for you:

[Image of a person looking frustrated with a caption that reads:]
"Bahot taqleef hoti jaati hai jab aap yogya ho aur koi aapki yogyata na pehchane... jab dost memes ka humor nahi samajh paate!"

Here's a meme text for you:

[Image of a person looking serious with a finger on their lips and a caption that reads:]
"Chup, bilkul chup... jab dost non-stop bak bak kar rahe hain aur aapko kuch bolne ka mouka nahi mil raha!"

Here's a meme text for you:

[Image of a person looking puzzled with a caption that reads:]
"Mera bet kya gaan ka ched jaisa dikta hai... jab kisi ki hairstyle bilkul perfect nahi hoti!"

Here's a meme text for you:

[Image of a person looking confident with a caption that reads:]
"Bharosa rakhiye, purane khiladi hai... jab dost 'chal  gym chale jayenge' bolke chhole bhatore dooste hain!"
Here's a meme text for you:

[Image of a person looking confused with a caption that reads:]
"Chaabhi kahan hai, gaan me dale ho kya chaabhi... jab kisi cheez ko dhundhne me laga hua ho!"
Apologies for that! Let's try another one:

[Image of a person looking annoyed with a caption that reads:]
"Accha baat nahi hai ye... jab friend phone ke charger ko ghuma ghuma ke dhundh raha ho, aur tum usi waqt uske haath mein dekh lo!"

Here's a meme text for you:

[Image of a person looking surprised with a caption that reads:]
"Ye kya bawasir bana diye ho... jab mai apna resume HR ko dikhata hoon!"
Here's a meme text for you:

[Image of a person looking shocked with a caption that reads:]
"Saala saanp ko paal raha tha... jab kisi ka business plan achha lag raha ho par phir pata chale, ki ho to ban chuka hai!"

Here's a meme text for you:

[Image of a person looking serious with a caption that reads:]
"Ab to sach bol bsdk... jab  office se leave lene ke liye bahane khatam ho gaye ho!"


Here's a meme text for you:

[Image of a person looking frustrated with a caption that reads:]
"Hindustan me jab tak cinema hai, log chutiya bante rahenge... jab koi unrealistic Bollywood scene dekhe aur us par vishwas kare!"

Of course! How about this:

[Image of a person looking relieved with a caption that reads:]
"Finally, khatam tata bye bye gaya... jab dost plans banakar pura weekend sone me nikal de!"

[Image of a boy having tears in his eyes with a caption reads:]
"Two days ago I changed my wifi password to hack it if you can and yesterday it was changed to challenge accepted!"







"""




nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
sentence_tokens=nltk.sent_tokenize(raw_text)
word_tokens=nltk.word_tokenize(raw_text)
lemmer=nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



greet_inputs=('hello','hi','whassup','namaste','kemchoo','how are you')
greet_responses=('hi','hey there',' i am fine', 'good','me too')
def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)



from sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robot_response= ' '
    TfidVec=TfidfVectorizer(tokenizer=LemNormalize,stop_words='english')
    tfidf=TfidVec.fit_transform(sentence_tokens)
    vals=cosine_similarity(tfidf[-1],tfidf)
    idx=vals.argsort()[0][-2]
    flat=vals.flatten()
    flat.sort()
    req_tfidf=flat[-2]
    if(req_tfidf==0):
        robot_response=robot_response+ "I am sorry.Unable to understand.please use more specific words in your prompt or remove typing error if any!"
        return robot_response
    else:
        robot_response=robot_response+sentence_tokens[idx]
        return robot_response
        
flag = True
print("Hello I am here to make you a bit more creative.Just ask the template text you want for your memes and add this template to your images!")
while(flag==True):
    user_response=input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thank you' or user_response=='thanks'):
            flag=False
            print('Bot: You are welcome!')
        else:
            if(greet(user_response) !=None):
               print('Bot:' + greet(user_response))
            else:
               sentence_tokens.append(user_response)
               word_tokens=word_tokens+nltk.word_tokenize(user_response)
               final_words=list(set(word_tokens))
               print('Bot:',end='')
               print(response(user_response))
               sentence_tokens.remove(user_response)
    else:
               flag = False
               print('Bot: Goodbye!')


return model
gr.Interface(model,inputs=gr.inputs.Textbox(lines=5,label="Input Text"),
outputs="text").launch()        