class person():
    def __init__ (self, name, age, favoritefood):
        self.name = name
        self.age = age
        self.favoritefood = favoritefood
        
    def introduce(self, ):
        print("我是"+ self.name+ "， 我今年"+ str(self.age)+ "歲，最喜歡吃"+ self.favoritefood)

    def shout(self, content):
        print("我大喊: ", content)
        

Amy = person("Amy", 15, "apple")
Amy.introduce()
Amy.shout(("我討厭看牙醫!"))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------