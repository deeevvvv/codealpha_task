def get_reply(user_input):
    text = user_input.lower().strip()

    if text == "hello" or text == "hi":
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text == "what is your name":
        return "I'm a simple chatbot."
    elif text == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def main():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Chatbot:", reply)

        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()