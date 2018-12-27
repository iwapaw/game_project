import storyStrings


class StoryGameScreen:  # a class that constructs a single instance of the game screen
    def __init__(self, string0, string1, string2, string3, string4, string5, string6, left, right):
        self.string0 = string0
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3
        self.string4 = string4
        self.string5 = string5
        self.string6 = string6
        self.left = left
        self.right = right


# passing the information to blit the current state of the game screen
currentScreen = StoryGameScreen(storyStrings.string0, storyStrings.string1, storyStrings.string2, storyStrings.string3,
                                storyStrings.string4, storyStrings.string5, storyStrings.string6, storyStrings.left,
                                storyStrings.right)

