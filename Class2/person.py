class Person:
    def __init__(self, hairColor, eyesColor):
        self.hairColor = hairColor
        self.eyesColor = eyesColor

    @classmethod 
    def American(cls):
        return cls("brown", "blue")
    
    @classmethod 
    def Taiwanese(cls):
        return cls("black", "black")
    def introduce(self):
        print("My eyes are {} and my hairs are {}." .format(self.eyesColor, self.hairColor))

Taiwanese = Person.Taiwanese()
American = Person.American()
Taiwanese.introduce()
American.introduce()