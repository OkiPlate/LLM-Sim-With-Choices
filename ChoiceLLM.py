import streamlit as st
import time
import numpy as np
import pandas as pd
import plotly.express as px

st.title("💬 Pepper")
st.caption("🚀 Your business advisor/consultant")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello, I'm Pepper and today I am going to guide you through solving a business case for Hunter LLC. But before we start, please let me know your name!"}]
    #st.session_state["messages"].append({"role": "assistant", "content": "But before we start, please let me know your name!"})
# Joo
# Func for displaying messages as typing
def stream_data(reply):
    for word in reply.split():
        yield word + " "
        time.sleep(0.1)

# Displaying past messages
for msg in st.session_state["messages"]:
     st.chat_message(msg["role"]).write(msg["content"])

numM = 1


# Handling new input

def introPart():
    #Intro Messages
    if len(st.session_state["messages"]) == 2 :
        reply = "Nice to meet you " + str(prompt) + "! Let's go ahead and get started working on this case."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
    

    if len(st.session_state["messages"]) == 3 :
        reply = "I’ll explain a bit about the company: Hunter LLC specializes in high-value financial solutions particularly for induviduals aiming to optimize their investments. They are a big company that's been in business for a couple of years now."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))   
    stillThereCheck()




#Check if user wants to continue 
def stillThereCheck():
    global numM 
    #Check if user wants to continue
    if len(st.session_state["messages"]) == 4 :
        reply = "Just to make sure you're still there, please reply 'yes' to continue."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 1
    if prompt.lower()  == "yes" and numM == 1:
        numM = 6
        continue1()
    elif prompt.lower() == "no" and numM == 1:
        reply = "Because we have limited time to solve this case, we have to focus on the task at hand. Please type 'yes' when you are ready to continue."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        continue1()
    elif prompt.lower() == "ready":
        numM = 15
        continue1()
    elif prompt.lower() == "a":
        reply = "We will go with Option A. I will go ahead and inform the client about our decision."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 18
        continue1()
    elif prompt.lower() == "b":
        reply = "We will go with Option B. I will go ahead and inform the client about our decision. Thank you for the cooperation"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 18
        continue1()
    

def plot_success_rates(success_rates):
    # Convert success rates to a DataFrame for plotting
    df = pd.DataFrame(list(success_rates.items()), columns=['Strategy', 'Success Rate'])
    
    # Create the bar chart using Plotly Express with additional customizations
    fig = px.bar(df, x='Strategy', y='Success Rate', 
                 labels={'Strategy': 'Strategy', 'Success Rate': 'Success Rate'}, 
                 title='Success Rates of Strategies',
                 text='Success Rate',  # This adds the text on the bars
                 color='Strategy',  # This assigns different colors based on the Strategy column
                 template='plotly_white')  # This uses the 'plotly_white' template for a clean look
    
    # Customize the layout
    fig.update_layout(
        xaxis_title='Strategy',
        yaxis_title='Success Rate',
        font=dict(family='Arial, sans-serif', size=12, color='RebeccaPurple'),
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        yaxis=dict(range=[0,1])  # Adjust y-axis to show full range from 0 to 1
    )
    
    # Customize bar appearance
    fig.update_traces(marker_line_width=1.5, opacity=0.6)  # Add border to bars and set opacity
    
    # Display the plot in Streamlit
    st.plotly_chart(fig)
    
# Main Body 1
def continue1():
    global numM      
    if numM == 6 :
        reply = "Great! Let's move on. We have a new client that has recently joined us and is looking forward to new investments. Recently we discussed the annual financial targets , setting the goals fo the upcoming year"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 8

    if numM == 8 :
        reply = "To achieve these, we've been evaluating various strategies and have narrowed down to two distinct strategies. However, we were hoping you could help us to finalize our approach."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM += 1

    if numM == 9 :
        reply = "Here are the two options we're considering:"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM += 1

    if numM == 10 :
        reply = "Option A: This option is safer and grows your money slowly. It’s like putting your money in a safe place where it can grow bit by bit."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM += 1

    if numM == 11 :
        reply = "Option B: This option is for taking chances to possibly make more money. It's riskier, but it could lead to better results."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM += 1

    if numM == 12 :
        reply = "Ok, so those are the options we have, I went ahead and calculated the success rates for each option. I would love to show them to you!"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM += 1

    if numM == 13 :
        reply = "Please type 'ready' when you are ready to see the success rates."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 14

    if numM == 15 :
        reply = "Great. So, according to my calculations, the success rate for Option A is 70%" + " and for Option B is 30%"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        success_rates = {"Option A": 0.8, "Option B": 0.6}
        plot_success_rates(success_rates)
        numM += 1

    if numM == 16 :
        reply = "Do you want to go with Option A or Option B?"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 17

    if numM == 18 :
        reply = "Thank you for your time and cooperation.  Have a great day!"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)
    
        


prompt = st.chat_input()

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    introPart()