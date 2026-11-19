import streamlit as st

from langchain_core.messages import HumanMessage, AIMessage

from chatbot import chat

# ---------------------------------
# PAGE CONFIGRATION
# ---------------------------------

st.set_page_config(
    page_title= "Gemini Chatbot",
    page_icon= "📊",
    layout= "centered"
)

# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("VIP ChatBot")

st.write(
    "Welcome to the Gemini Chatbot! Ask me anything and I'll do my best to help you."
    )

# -------------------------------------------------
# Initialize Memory
# ------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# ------------------------------------------------
# Display Previous Conversation
# ------------------------------------------------

for message in st.session_state.history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# -------------------------------------------------
# USER INPUT
# -------------------------------------------------

user_input = st.chat_input("Type your message here......")

# -------------------------------------------------
# GENERATE RESPONSE
# ------------------------------------------------

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Show AI response
    response = chat(
        user_input, st.session_state.history
    )

    #Save user message
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.history.append(
        HumanMessage(content=user_input)
    )

    # Save AI response
    st.session_state.history.append(
        AIMessage(content=response)
    )