from dotenv import load_dotenv# use to excess the key 
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("Google_api_key"))

#function to load gemini model and get response
model=genai.GenerativeModel("gemini-pro")

chat=model.start_chat(history=[])#save the history

def get_response(question):
    response=chat.send_message(question,stream=True)# stream true because we want to show quickly to the webpage
    return response


st.set_page_config(page_title="QnA demo")
st.header("ASK THE QUESTION ")

if 'chat_history' not in st.session_state:#use to save the history
    st.session_state['chat_history'] = []

input=st.text_input("INPUT:",key="input")
submit=st.button("Ask the question")

if submit and input:
    response=get_response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)# jese jese response aaye vese print hota rahe
        st.session_state['chat_history'].append(("Bot", chunk.text))# history me save hota rhe
# st.subheader("CHAT HISTORY")
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")
     
