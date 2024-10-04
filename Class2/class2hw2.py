class homework():
    def __init__(self, Homework, stats):
        self.Homework = Homework
        self.stats = stats

    def write(self):
        self.__class__.homework = "I am done with my homework."
        self.__class__.stats = "Done"
    def writehalf(self):
        self.__class__.homework = "I almost finished my homework."
        self.__class__.stats = "In Progress"
    def didntwrite(self):
        self.__class__.homework = "I forgot to do my homework."
        self.__class__.stats = "Undo"
    @classmethod 
    def Lucas4(cls):
        return cls("I almost finished my homework", "In Progress")
    @classmethod 
    def Lucas5(cls):
        return cls("I am done with my homework", "Done")
    def introduce(self):
        print(self.Homework)

Lucas1 = homework("didn't start yet", "undo")
Lucas2 = homework("didn't start yet", "undo")
Lucas3 = homework("didn't start yet", "undo")
Lucas4 = homework.Lucas4()
Lucas5 = homework.Lucas5()
Lucas1.write()
print(homework.homework)
print("Homework status:", homework.stats)
Lucas2.writehalf()
print(homework.homework)
print("Homework status:", homework.stats)
Lucas3.didntwrite()
print(homework.homework)
print("Homework status:", homework.stats)
Lucas4.introduce()
Lucas5.introduce()