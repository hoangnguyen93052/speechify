import openai
import json
import random
import os

class AIGenerator:
    def __init__(self, api_key, model="text-davinci-003"):
        openai.api_key = api_key
        self.model = model

    def generate_text(self, prompt, max_tokens=150):
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()

class PromptManager:
    def __init__(self, prompt_file):
        self.prompt_file = prompt_file
        self.prompts = self.load_prompts()

    def load_prompts(self):
        with open(self.prompt_file, 'r') as file:
            return json.load(file)

    def get_random_prompt(self):
        return random.choice(self.prompts)

class UserInterface:
    def __init__(self):
        self.prompt_manager = PromptManager("prompts.json")
        self.ai_generator = AIGenerator(api_key=os.getenv("OPENAI_API_KEY"))

    def start(self):
        print("Welcome to the AI Text Generator!")
        while True:
            user_input = input("Press 'g' to generate a text or 'q' to quit: ")
            if user_input.lower() == 'g':
                self.generate_text()
            elif user_input.lower() == 'q':
                print("Exiting the program.")
                break
            else:
                print("Invalid input. Please try again.")

    def generate_text(self):
        prompt = self.prompt_manager.get_random_prompt()
        print(f"Using prompt: {prompt}")
        generated_text = self.ai_generator.generate_text(prompt)
        print(f"Generated text:\n{generated_text}\n")

if __name__ == "__main__":
    ui = UserInterface()
    ui.start()

# Sample prompts.json
# [
#   "Once upon a time, in a future not so far away,",
#   "In a world where AI ruled the daily lives of humans,",
#   "The discovery of a new planet led to unexpected consequences.",
#   "Beneath the city, secrets lingered long forgotten.",
#   "It was a dark and stormy night when the lights went out."
# ]