import tkinter as tk
from story import Story
import story_data

class InteractiveStoryGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.story = Story(story_data.story_data)
        self.choices_made = []
        self.story.state = "introduction"  # Add this line
        self.create_widgets()

    def make_choice(self, choice):
        self.story.state = self.story.story_data[self.story.state]["choice"][choice]
        self.choices_made.append(choice)
        for button in self.choice_buttons:
            button.destroy()
        self.choice_buttons.clear()
        self.display_scene()


    def create_widgets(self):
        self.choice_buttons = []
        self.text = tk.Text(self, wrap=tk.WORD, height=10, width=50)
        self.text.pack(padx=10, pady=10)
        self.display_scene()

    def display_scene(self):
        current_scene = self.story.story_data[self.story.state]
        description = f"{current_scene['description']}\n"
        #description = f"Scene: {current_scene['scene']}\n\nEvent: {current_scene.get('event', '')}\n\nDescription: {current_scene['description']}\n"
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, description)

        if "choice" in current_scene:
            for idx, choice in enumerate(current_scene["choice"], 1):
                button = tk.Button(self, text=choice.capitalize().replace('_', ' '), command=lambda choice=choice: self.make_choice(choice))
                button.pack(side=tk.LEFT, padx=5, pady=5)
                self.choice_buttons.append(button)
        else:
            self.display_conclusion()

    def handle_user_input(self, user_choice):
        self.choices_made.append(user_choice)
        self.story.state = self.story.story_data[self.story.state]["choice"][user_choice]
        self.display_scene()

    def display_conclusion(self):
        last_choice = self.choices_made[-1] if self.choices_made else "Default Outcome"
        choice_node_key = self.story.story_data["final_tower_t_s_t_v"]["choice"][last_choice]
        conclusion_node = self.story.story_data[choice_node_key]
    
        self.text.delete(1.0, tk.END)
        #self.text.insert(tk.END, f"Scene: {conclusion_node['scene']}\n")
        self.text.insert(tk.END, f"{conclusion_node['description']}\n")



    #def display_conclusion(self):
     #   conclusion_node = self.story.story_data["conclusion_e_t_s_t_v"]
      #  chosen_outcome = conclusion_node["outcome"].get(self.choices_made[-1], "Default Outcome") if self.choices_made else "Default Outcome"
      #  self.text.delete(1.0, tk.END)
       # self.text.insert(tk.END, f"Scene: {conclusion_node['scene']}\n")
        #self.text.insert(tk.END, f"Outcome: {chosen_outcome}\n")
        #self.text.insert(tk.END, f"Description: {conclusion_node['description']}\n")

root = tk.Tk()
app = InteractiveStoryGUI(master=root)
app.mainloop()
