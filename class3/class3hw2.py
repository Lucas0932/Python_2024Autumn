class Sport:
    def __init__(self, sport, hours):
        self.sport = sport
        self.hours = hours
    @staticmethod
    def play(sport, hours):
        print("PLaying", sport, "takes", hours, "hours.") 

class Baseball(Sport): 
    def __init__(self, sport, hours):
        super().__init__(sport, hours) #1
        self.sport = "baseball"
        self.hours = 4

class Basketball(Sport): 
    def __init__(self, sport, hours):
        super().__init__(sport, hours) #1
        self.sport = "basketball"
        self.hours = 2
Baseball = Sport(Baseball, 2)
Baseball.play("baseball", 2)
Basketball = Sport(Basketball, 4)
Basketball.play("basketball", 4)