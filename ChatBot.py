import openai

class ChatBot:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_bot_response(self, user_input, chat_history=[]):
        chat_history.append(user_input)

        response = openai.Completion.create(
            engine="text-davinci-002",  # You can use other engines depending on your subscription plan.
            prompt="\n".join(chat_history),
            temperature=0.7,
            max_tokens=150,
            stop=["\n"]
        )

        bot_response = response.choices[0].text.strip()
        chat_history.append(bot_response)

        return bot_response

def main():
    # Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
    api_key = 'YOUR_OPENAI_API_KEY'
    chat_bot = ChatBot(api_key)
    print("ChatBot: Hello! How can I assist you today? (Type 'bye' to exit)")

    chat_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! Have a great day.")
            break

        bot_response = chat_bot.get_bot_response(user_input, chat_history)
        print("ChatBot:", bot_response)

if __name__ == "__main__":
    main()
