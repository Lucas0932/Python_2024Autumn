from flask import Flask

app = Flask(__name__) # 建立 app 變數為 Flask 物件，__name__ 表示目前執行的程式

@app.route("/") # 使用函式裝飾器，建立一個路由 ( Routes )，可針對主網域 / 發出請求
def home(): # 發出請求後會執行 home() 的函式
    return "<h1>hello world</h1>"# 執行函式後會回傳特定的網頁內容，以HTML格式以方便瀏覽器來做網頁的展示

#app.run() # 執行

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