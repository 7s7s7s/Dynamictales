import story_data
from story import Story

def main():
    story = Story(story_data.story_data)
    current_scene = "introduction"
    choices_made = []

    while current_scene != "conclusion":
        scene_data = story.story_data[current_scene]

        # Print the scene's description and any events
        print("\nScene:", scene_data["scene"])
        if "event" in scene_data:
            print("Event:", scene_data["event"])
        print("Description:", scene_data["description"])

        # If there are choices, present them to the user
        if "choice" in scene_data:
            print("\nOptions:")
            for idx, choice in enumerate(scene_data["choice"], 1):
                print(f"{idx}. {choice.capitalize().replace('_', ' ')}")

            # Get user input
            user_input = int(input("\nEnter the number of your choice: "))
            user_choice = list(scene_data["choice"].keys())[user_input - 1]
            choices_made.append(user_choice)

            # Move to the next scene
            current_scene = scene_data["choice"][user_choice]
        else:
            current_scene = "conclusion"

    # Print the conclusion
    conclusion_node = story.story_data["conclusion"]
    chosen_outcome = conclusion_node["outcome"].get(choices_made[-1], "Default Outcome") if choices_made else "Default Outcome"
    print("\nScene:", conclusion_node["scene"])
    print("Outcome:", chosen_outcome)
    print("Description:", conclusion_node["description"])
    
if __name__ == "__main__":
    main()
