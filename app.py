import google.genaretiveai as genai

API_KEY = "AIzaSyCKkCWBOMQhckvf6u-ctkUeMfbo7fpueEY"

genai.configure(api_key = API_KEY)

model = genai.Model("gemini-2.0-flash")

chat = model.start_chat()

print("Welcome to the Gemini 2.0 Flash model chat!")