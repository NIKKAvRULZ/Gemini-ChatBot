import google.generativeai as genai
API_KEY = "AIzaSyCKkCWBOMQhckvf6u-ctkUeMfbo7fpueEY"

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

response = chat.send_message("What is the capital of France?")

print("Gemini : ",response.text)