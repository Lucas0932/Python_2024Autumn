import abc

class Sport(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod # 限制他的子類別，一定要實作talk的方法
    def play(self):
        pass

class Basketball(Sport):
    def play(self):
        print("Playng basketball takes 2 hours.")

class Baseball(Sport):
    def play(self):
        print("Playng baseball takes 4 hours.")

basketball = Basketball()
baseball = Baseball()
basketball.play()
baseball.play()