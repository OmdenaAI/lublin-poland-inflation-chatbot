import streamlit as st
from streamlit_chat import message
import requests
import openai

st.set_page_config(
    page_title="Omdena Lublin Chapter: Financial Chatbot",
    page_icon=":robot:"
)

#API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
#headers = {"Authorization": st.secrets['api_key']}

st.header("Omdena Lublin Chapter: Financial Chatbot")
#st.markdown("[Github](https://github.com/ai-yash/st-chat)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

#def query(payload):
#	response = requests.post(API_URL, headers=headers, json=payload)
#	return response.json()

def get_text():
    input_text = st.text_input("What is your question?", key="input")
    return input_text 


def model_response(question):
    
    start_sequence = "A:"
    restart_sequence = "\n\nQ: "
    response = openai.Completion.create(
    model= st.secrets["model"],
    api_key = st.secrets["model"],
    prompt=restart_sequence+question+'\n\n###\n\n',
    temperature=0,
    # max tokens as response
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    #if you insert '.' or new line this means you quit the chat. so do not insert a "." or a new line at the end of your question
    stop=[".","\n"]
    )
    return response['choices'][0]['text']

user_input = get_text()

if user_input:
    output = model_response(user_input)

    st.session_state.past.append(user_input)
        #st.session_state.generated.append(output["generated_text"])
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
