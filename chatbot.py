import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# LLM

llm = ChatGoogleGenerativeAI(
    model= "gemini-3.8-flash",
    temprature= 0.7
)

# PROMPT

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a friendly and helpful Ai assistant.
    
        Remember the conversation history and use to answer to the user's question naturally
    
        If the answer is not avilable from the conversation, answer normally using you general knowledge"""
    ),
    
    MessagesPlaceholder(variable_name="history"),

    ("human","{input}")
    ])

# CHAIN

chain = prompt | llm

# CHAT FUNCTION

def chat(input_text, history):

    response = chain.invoke({
        "history": history,
        "input": input_text
    })

    # Convert Gemini response into plain text
    if isinstance(response.content, str):
        return response.content

    # Handle newer Gemini content-block format
    if isinstance(response.content, list):

        text_parts = []

        for block in response.content:

            if isinstance(block, dict) and block.get("text"):
                text_parts.append(block["text"])

        return "".join(text_parts)

    return str(response.content)
