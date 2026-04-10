import requests

API_KEY = "AIzaSyCvNeRUWPUBy63c7tvRlZ4-PpT50UvU2Dg"

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

headers = {
    "x-goog-api-key": API_KEY,
    "Content-Type": "application/json"
}

while True:
    user_input = input("-> ")
    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if "candidates" in data:
        reply = data["candidates"][0]["content"]["parts"][0]["text"]
        print("Bot:", reply)
    else:
        print("Error:", data)