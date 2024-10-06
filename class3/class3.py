class Person:
    @staticmethod
    def work(work_hour):
        print("Working hours:", work_hour)

amy = Person()
amy.work(8)
#--------------------------------------------------------------------------
class Student:
    def __init__(self, name):
        self.__name = name
        self.__score = {"Math": 0, "Physics": 0, "Chemistry": 0}
    #私有方法
    def __add_subject(self, subject):
        self.__score[subject] = 0
    #公有方法
    def set_score(self, subject, score):
        if subject not in self.__score:
            self.__add_subject(subject)
        self.__score[subject] = score

    def get_subject(self):
        for key in self.__score:
            print(key, self.__score[key])
Lucas = Student("Lucas")
Lucas.set_score("Chinese", 100)
Lucas.get_subject()
#--------------------------------------------------------------------------
#被繼承的類別 -> 父類別
class Person: # 1
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.__ID = ID
    def speak(self, sentence):
        return self.name + "says" + sentence
    
#繼承 Person 的類別 -> 子類別
class Athlete(Person): #2
    #覆寫建構子
    def __init__(self, name, age, ID, height):
        super().__init__(name, age, ID) #1
        self.height = height
    def workout(self):
        return "%s goes to the gym to exercise." % (self.name)
    #覆寫 speak 的方法
    def speak(self, sentence):
        print("Athelete: ", super().speak(sentence)) #2
Lucas = Athlete("Lucas", 13, "yay", 180)
Lucas.speak(" hello!")
Lucas.workout()
#--------------------------------------------------------------------------
import abc
class Member(metaclass = abc.ABCMeta):
    def __init__(self, name, level):
        self.name = name
        self.level = level
    @abc.abstractclassmethod
    def discount(self, price):
        pass
    