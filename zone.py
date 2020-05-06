class Zone:
    def __init__(self, name, introtext, enemies = []):
        self.name = name
        self.introtext = introtext
        self.enemies = enemies
    
    def intro(self):
        print(self.introtext)

class Intro(Zone):
    def intro(self):
        print(self.introtext)
        valid_input = False
        print("If you would like additional help before starting the game, please input \"Help\". Otherwise, please press return.")
        while not valid_input:
            user_action = input("> ")
            if user_action == "Help":
                print("This is placeholder text for Help")
                valid_input = True
            elif user_action == "":
                valid_input = True
            else:
                print("That is not a valid input.")
            