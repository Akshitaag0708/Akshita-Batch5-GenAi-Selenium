from inte_api import get_response

print("Chatbot started (type 'exit' to quit)")

while True:
    user_input = input("-> ")

    if user_input.lower() == "exit":
        print("Chat ended")
        break

    reply = get_response(user_input)
    print("**", reply)