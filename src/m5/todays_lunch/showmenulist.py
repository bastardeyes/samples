from m5stack import *
import random
import gc
from jpfont import jpfont

class ShowMenuList:

    def __init__(self):
        self.fortunelist=["大吉","中吉","小吉","末吉","吉"]
        self.menulist=["肉","魚","定食","丼","米","中華","和食","洋食","イタリアン","エスニック","麺類","カレー味","ビル出て右","ビル出て左","赤いもの","白いもの","茶色いもの","黄色いもの","温かいもの","女子力高いもの","おっさん飯","居酒屋めし","からいもの","とろみがある","ビル1F","2F以上","ビル地下","ファミレス","スプーンで食う","おばちゃん店員","900円以内"]
        self.jpfontObj = jpfont()
        self.backimg="/flash/assets/food_gohan.jpg"

        lcd.clear()
        lcd.image(0, 0,self.backimg)
        lcd.setCursor(0, 0)
        lcd.setColor(lcd.BLACK)
        menu=random.choice(self.menulist)

        buttonA.wasPressed(self.on_AwasPressed)
        buttonB.wasPressed(self.on_BwasPressed)
        buttonC.wasPressed(self.on_CwasPressed)


    def on_AwasPressed(self): #選択肢なし
        self.printMenues(1)

    def on_BwasPressed(self): #2択
        self.printMenues(2,options=["奇数","偶数"])

    def on_CwasPressed(self): #3択
        self.printMenues(3,options=["Ａ","Ｂ","Ｃ"])


    def printMenues(self, freq=1,options=None):
        lcd.image(0, 0, self.backimg)

        if freq==1: 
            self.jpfontObj.printString("【今日のごはん占い】", 4, 4)
            fortune="＊＊ {0} ＊＊".format(random.choice(self.fortunelist))
            self.jpfontObj.printString(fortune, 4, 20)
            self.jpfontObj.printString("＊ 本日のおすすめ？ ＊", 4, 40)
            menu=random.choice(self.menulist)
            self.jpfontObj.printString(menu, 4, 60)

        else :
            self.jpfontObj.printString("【今日のごはんチャレンジ】", 4, 4)
            self.jpfontObj.printString("ダイスで決めようぜ!", 4, 20)
            self.jpfontObj.printString("＊ 選択肢 ＊", 4, 40)

            for i in range(freq):
                menu=random.choice(self.menulist)
                text="{0}){1}".format(options[i],menu)
                self.jpfontObj.printString(text, 4, 60 + i*20)

        gc.collect()

    