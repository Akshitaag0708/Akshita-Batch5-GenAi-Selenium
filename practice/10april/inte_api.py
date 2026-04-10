import requests

API_KEY = "AIzaSyCvNeRUWPUBy63c7tvRlZ4-PpT50UvU2Dg"

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

HEADERS = {
    "x-goog-api-key": API_KEY,
    "Content-Type": "application/json"
}

def get_response(user_input):
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }

    try:
        response = requests.post(URL, headers=HEADERS, json=payload)
        data = response.json()

        if "candidates" in data:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"Error: {data}"

    except Exception as e:
        return f"Exception occurred: {str(e)}"