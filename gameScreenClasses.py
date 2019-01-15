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

    @staticmethod
    def current_screen_setter():
        setattr(currentScreen, 'string0', storyStrings.gameScreenStringDictionary.get("string0"))
        setattr(currentScreen, 'string1', storyStrings.gameScreenStringDictionary.get("string1"))
        setattr(currentScreen, 'string2', storyStrings.gameScreenStringDictionary.get("string2"))
        setattr(currentScreen, 'string3', storyStrings.gameScreenStringDictionary.get("string3"))
        setattr(currentScreen, 'string4', storyStrings.gameScreenStringDictionary.get("string4"))
        setattr(currentScreen, 'string5', storyStrings.gameScreenStringDictionary.get("string5"))
        setattr(currentScreen, 'string6', storyStrings.gameScreenStringDictionary.get("string6"))
        setattr(currentScreen, 'left', storyStrings.gameScreenStringDictionary.get("left"))
        setattr(currentScreen, 'right', storyStrings.gameScreenStringDictionary.get("right"))

    @staticmethod
    def current_screen_updater():
        StoryGameScreen.currentScreen = StoryGameScreen(storyStrings.string0,
                                                        storyStrings.string1,
                                                        storyStrings.string2,
                                                        storyStrings.string3,
                                                        storyStrings.string4,
                                                        storyStrings.string5,
                                                        storyStrings.string6,
                                                        storyStrings.left,
                                                        storyStrings.right)
        return StoryGameScreen.currentScreen


currentScreen = StoryGameScreen.current_screen_updater()



