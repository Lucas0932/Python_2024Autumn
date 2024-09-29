class homework():
    Homework = "didn't start yet"
    stats = "undo"

    def write(self):
        self.__class__.homework = "I am done with my homework."
        self.__class__.stats = "Done"
    def writehalf(self):
        self.__class__.homework = "I almost finished my homework."
        self.__class__.stats = "In Progress"
    def didntwrite(self):
        self.__class__.homework = "I forgot to do my homework."
        self.__class__.stats = "Undo"

Lucas1 = homework()
Lucas2 = homework()
Lucas3 = homework()
Lucas1.write()
print(homework.homework)
print("Homework status:", homework.stats)
Lucas2.writehalf()
print(homework.homework)
print("Homework status:", homework.stats)
Lucas3.didntwrite()
print(homework.homework)
print("Homework status:", homework.stats)