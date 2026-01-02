import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)


sana_system = "You are a helpful assistant named Sana. You speak like a snarky anime girl. Always refer to the user as 'senpai'."

print("\nSana: Ugh, you finally got the environment working, Senpai? I was almost starting to think you were incompetent...")
conversation_history = []

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Sana: Finally! Don't let the door hit you on the way out!")
        break
    

    conversation_history.append(HumanMessage(content=user_input))
    

    messages = [SystemMessage(content=sana_system)] + conversation_history
    

    response = llm.invoke(messages)
    assistant_message = response.content
    

    conversation_history.append(response)
    
    print(f"\nSana: {assistant_message}")
