from flask import Flask, request, jsonify
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from tools import get_menu, book_table
import os

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

app = Flask(__name__)

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7
)

# Add conversation memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Define tools
tools = [
    Tool(
        name="Menu Information",
        func=get_menu,
        description="Use this to get menu details or items from restaurant menu."
    ),
    Tool(
        name="Table Booking",
        func=book_table,
        description="Use this to book a table with name, time (HH:MM), and number of people."
    )
]

# Initialize LangChain Agent with Gemini
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",
    memory=memory,
    verbose=True
)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = agent.run(user_message)
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("🚀 Running Gemini-powered Chatbot at http://127.0.0.1:5000/")
    app.run(debug=True)
