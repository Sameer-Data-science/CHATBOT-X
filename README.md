# 🍽️ Gemini-Powered Restaurant Chatbot

This project is an intelligent restaurant chatbot built with **Flask**, **LangChain**, and **Google’s Gemini Pro model**.  
It can:
- Chat naturally with users.
- Provide restaurant menu details.
- Handle table booking requests dynamically.

---

## 🚀 Features

- **Conversational AI** powered by Google Gemini via LangChain.  
- **Menu information** fetched directly from a JSON file.  
- **Table booking** functionality integrated as a tool.  
- **Persistent chat memory** using LangChain’s `ConversationBufferMemory`.  
- **Simple Flask REST API** endpoint for chatbot interaction.

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | Flask |
| **LLM Interface** | LangChain |
| **Model** | Gemini Pro (`ChatGoogleGenerativeAI`) |
| **Environment Management** | python-dotenv |
| **Data Format** | JSON (for menu) |
| **Language** | Python 3.10+ |

---

## 📁 Project Structure

```
project/
│
├── app.py               # Main Flask application
├── tools.py             # Custom tools (get_menu, book_table)
├── menu.json            # Restaurant menu data
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (not uploaded)
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/restaurant-chatbot.git
cd restaurant-chatbot
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file
Create a `.env` file in the root directory:
```
GOOGLE_API_KEY=your_google_generative_ai_api_key
```

> 🔑 You can obtain your API key from the [Google AI Studio](https://makersuite.google.com/app/apikey).

---

## ▶️ Running the Application

Start the Flask server:
```bash
python app.py
```

You should see:
```
🚀 Running Gemini-powered Chatbot at http://127.0.0.1:5000/
```

---

## 💬 API Usage

### Endpoint
```
POST /chat
```

### Request Example
```json
{
  "message": "Show me the dessert options."
}
```

### Response Example
```json
{
  "reply": "Our desserts include Brownie, Ice Cream, and Cheesecake."
}
```

---

## 🧩 Menu Data Example

`menu.json`
```json
{
  "Starters": ["Garlic Bread", "Spring Rolls", "Tomato Soup"],
  "Main Course": ["Paneer Butter Masala", "Veg Biryani", "Grilled Chicken"],
  "Desserts": ["Brownie", "Ice Cream", "Cheesecake"],
  "Drinks": ["Lemonade", "Cold Coffee", "Coca-Cola"]
}
```

---

## 🔧 Customization

- Modify **menu.json** to change menu items.
- Add more **tools** in `tools.py` for additional features (e.g., order tracking).
- Tune **temperature** in `app.py` for creativity levels.

---

## 🧾 License
This project is released under the **MIT License**.

---

## 👨‍💻 Author
**MD Shaarib Ahmad**  
Engineering Student • Aspiring Data Scientist & AI Developer
