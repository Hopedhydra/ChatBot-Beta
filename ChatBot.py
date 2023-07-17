import random
import json
from googlesearch import search

class ChatBot:
    # ... (existing code)

    def search_on_internet(self, query):
        search_results = list(search(query, num=3, stop=3, pause=2))
        if not search_results:
            return "I couldn't find any relevant information on the internet."

        return f"I found some links that might help:\n{chr(10).join(search_results)}"

    def get_bot_response(self, user_input):
        user_input = user_input.lower()

        if "" in user_input:
            query = user_input.replace("search the web for", "").strip()
            return self.search_on_internet(query)

        for question, responses in self.bot_responses.items():
            if question in user_input:
                return random.choice(responses)

        return self.learn_response(user_input)

    # ... (existing code)

def main():
    # ... (existing code)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! Have a great day.")
            break

        response = chat_bot.get_bot_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()

