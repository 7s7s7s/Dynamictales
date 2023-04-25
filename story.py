# In story.py
import story_data

class Story:
    def __init__(self, story_data):
        self.story_data = story_data
        self.state = None

    def set_state(self, state):
        self.state = state


    def handle_user_input(self, user_input):
        choices = story_data.story_data[self.state].get("choice")
        if choices:
            try:
                selected_choice_key = list(choices.keys())[int(user_input) - 1]
                return selected_choice_key
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid choice number.")
                return None
        else:
            return None

    def update_story_state(self, user_choice):
        if user_choice:
            next_state = self.story_data[self.state]["choice"][user_choice]
            if next_state == "conclusion":
                self.set_conclusion_state(user_choice)
            else:
                self.state = next_state


    def generate_story_prompt(self):
        scene = self.story_data[self.state]["scene"]
        event = self.story_data[self.state].get("event")
        prompt = f"Scene: {scene}\n"
        if event:
            prompt += f"Event: {event}\n"

        choices = self.story_data[self.state].get("choice")
        if choices:
            prompt += "\nChoose an option:"
            for i, choice in enumerate(choices.values(), 1):
                prompt += f"\n{i}. {choice}"

        return prompt

    def is_finished(self):
        return self.state == "conclusion"

    def get_node(self, node_key):
        return self.story_data[node_key]

    def play(self):
        while not self.is_finished():
            prompt = self.generate_story_prompt()
            print(prompt)

            user_input = input("\nEnter your choice or response: ")

            user_choice = self.handle_user_input(user_input)
            self.update_story_state(user_choice)

        print("The story has reached its conclusion.")
        outcome_key = list(self.story_data[self.state]["outcome"].keys())[0]
        print(self.story_data[self.state]["outcome"][outcome_key])

    def set_conclusion_state(self, state):
        self.conclusion_state = state

