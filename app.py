import google.generativeai as genai
API_KEY = "AIzaSyCKkCWBOMQhckvf6u-ctkUeMfbo7fpueEY"

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

print("Welcome to Gemini 2.0 Flash Chatbot!")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Exiting chat.")
        break
    response = chat.send_message(user_input)
    print("Gemini : ", response.text)
