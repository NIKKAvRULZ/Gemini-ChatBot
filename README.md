# 💬 Gemini 2.0 Flash Chatbot

This is a simple terminal-based chatbot powered by **Google Gemini 2.0 Flash** using the `google.generativeai` Python SDK. It enables users to interact with Gemini AI directly from the command line in a continuous chat format.

---

## 📌 Features

- ✅ Simple command-line interface (CLI)
- ✅ Continuous conversation with context retention
- ✅ Uses Gemini 2.0 Flash model for fast and intelligent responses
- ✅ Easy-to-configure API key support

---

## 🛠️ Requirements

- Python 3.7+
- `google-generativeai` Python package

Install the required package via:

```bash
pip install google-generativeai
```

---

## 🚀 Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
```

2. **Add your Gemini API key**

Replace the placeholder API key in the script with your own:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

> 🔐 **Warning**: Never expose your real API key in public repositories. Consider using environment variables for better security.

3. **Run the chatbot**

```bash
python gemini_chatbot.py
```

4. **Start chatting!**

Type your messages in the terminal. To end the session, type:

```text
exit
```

---

## 🧠 Example Usage

```text
Welcome to Gemini 2.0 Flash Chatbot!
You: What is the capital of France?
Gemini :  The capital of France is Paris.
You: exit
Exiting chat.
```

---

## 🧑‍💻 Code Overview

```python
import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini : ", response.text)
```

---

## 📬 Contact

For questions, reach out at [your-email@example.com](mailto:nithika151@gmail.com) or connect via [LinkedIn](https://www.linkedin.com/in/nithika-perera-519197254).

---

## ⭐️ Support

If you find this project useful, please consider giving it a ⭐ on GitHub!
