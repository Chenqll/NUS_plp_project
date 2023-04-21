import streamlit as st
from streamlit_chat import message
import requests



# app related codes in mian()
def main(): 
    # set page config
    st.set_page_config(
        page_title="AI Author Chats",
        page_icon="https://drive.google.com/file/d/1RYrYzac43C1XB_j31drsjsCsU21UpRLU/view?usp=share_link", #url of the logo
        #layout="wide",
        #initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# Any question? Ask the auther!"
        }
    )
    
    # can load model here #
    
    st.title("Any question? Ask the auther!")
    st.write("AI Author Chats")

    # ask a question through side bar
    st.sidebar.info('You may ask...')

    book_brief = 'What is the book about?'
    book_brief_button = st.sidebar.button(book_brief)

    chapter_sum = 'Summarize the chapters for me'
    chapter_sum_button = st.sidebar.button(chapter_sum)

    author_intro = 'Tell me about yourself'
    author_intro_button = st.sidebar.button(author_intro)

    read_time = 'How long does it take to finish this book?'
    read_time_button = st.sidebar.button(read_time)

    intended_reader = 'Who are the intended readers?'
    intended_reader_button = st.sidebar.button(intended_reader)

    key_characters = 'The key characters in the story'
    key_characters_button = st.sidebar.button(key_characters)



    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    
    def get_text():
        input_text = st.text_input("You: ", placeholder='Send a message...', key="input",label_visibility="collapsed")
        return input_text 
   
    user_input = get_text()

    
    if chapter_sum_button:
        button_question = chapter_sum
        output = button_question # output = input
        st.session_state.past.append(button_question)
        st.session_state.generated.append(output)

    elif book_brief_button:
        button_question = book_brief
        output = button_question  # output = input
        st.session_state.past.append(button_question)
        st.session_state.generated.append(output)

    elif author_intro_button:
        button_question = author_intro
        output = button_question  # output = input
        st.session_state.past.append(button_question)
        st.session_state.generated.append(output)

    elif read_time_button:
        button_question = read_time
        output = button_question  # output = input
        st.session_state.past.append(button_question)
        st.session_state.generated.append(output)   
    
    elif intended_reader_button:
        button_question = intended_reader
        output = button_question  # output = input
        st.session_state.past.append(button_question)
        st.session_state.generated.append(output)     
   
    elif key_characters_button:
        button_question = key_characters
        output = button_question  # output = input
        st.session_state.past.append(button_question)
        st.session_state.generated.append(output)

    elif user_input:
        output = user_input  # output = input
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)




    if st.session_state['generated']:

        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i)) #chatbot's answer appears on the left
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user') #user's input appears on the right



if __name__ == '__main__':
    main()