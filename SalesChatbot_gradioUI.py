import gradio as gr
import random
import time


with gr.Blocks() as demo:
    gr.Markdown('# Any question? Ask the author!')
    chatbot = gr.Chatbot(label = 'AI Author Chats')
    msg = gr.Textbox(label="Send a message...")
    clear = gr.Button("Clear")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def bot(history):
        bot_message = history[-1][0] # set bot's message to user's input # output = input
        history[-1][1] = ""
        for character in bot_message:
            history[-1][1] += character
            time.sleep(0.05)
            yield history
            
    examples = gr.Examples(examples=["What is the book about?", "Summarize the chapters for me","Tell me about yourself","How long does it take to finish this book?","Who are the intended readers?",'The key characters in the story'],
                           inputs = msg, label = 'You may ask...')
            

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

demo.queue()
demo.launch(share=True)
