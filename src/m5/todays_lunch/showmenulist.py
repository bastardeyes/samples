from m5stack import *
from machine import I2C, Pin
from mpu9250 import MPU9250
import time
import math
import random
import gc
from jpfont import jpfont

class ShowMenuList:
    def __init__(self):
        self.fortunelist=["大吉","中吉","小吉","末吉","吉"]
        self.menulist=["肉","魚","定食","丼","米","中華風","和風","洋風","イタリアン","エスニック","麺類","カレー味","ビル出て右","ビル出て左","赤いもの","白いもの","茶色いもの","黄色いもの","温かいもの","女子力高いもの","おっさん飯","居酒屋めし","からいもの","とろみがある","ビル1F","2F以上","ビル地下","ファミレス","スプーンで食う","おばちゃん店員","900円以内"]
        self.challengedict={0:{"方法":"ダイスで決めようぜ!","選択肢":["偶数","奇数"]},
                            1:{"方法":"近くの人とジャンケン","選択肢":["勝ち","負け"]},
                            2:{"方法":"AかつB","選択肢":["A","B"]}}
        self.jpfontObj = jpfont()

        #いらすとや再頒布NGのため、いらすとやで「ご飯」を検索してDLしてください。pngでは表示されません。
        self.backimg="/flash/assets/food_gohan.jpg"

        self.i2c = I2C(sda = 21, scl = 22)
        self.sensor = MPU9250(self.i2c)

        lcd.clear()
        lcd.image(0, 0,self.backimg)
        lcd.setCursor(0, 0)
        lcd.setColor(lcd.BLACK) 

        buttonA.wasPressed(self.on_AwasPressed)
        buttonB.wasPressed(self.on_BwasPressed)
        buttonC.wasPressed(self.on_CwasPressed)


    def on_AwasPressed(self): #選択肢なし
        self.printMenues(1)

    def on_BwasPressed(self): #2択
        self.printMenues(2)

    def on_CwasPressed(self): #3択
        self.printMenues(3,options=["Ａ","Ｂ","Ｃ"])

    def printMenues(self, freq=1,options=None):
        lcd.image(0, 0, self.backimg)
        correction_val=self.get_correction_val()
        selected_menues=[]

        if freq==1: 
            self.jpfontObj.printString("【今日のごはん占い】", 4, 4)
            num= (random.randint(0, 100) + correction_val) % len(self.fortunelist)
            fortune="＊＊ {0} ＊＊".format(self.fortunelist[num])

            self.jpfontObj.printString(fortune, 4, 20)
            self.jpfontObj.printString("＊ 本日のおすすめ？ ＊", 4, 40)
            menu=self.get_menu(correction_val,selected_menues)
            self.jpfontObj.printString(menu, 4, 60)

        elif freq==2:
            self.jpfontObj.printString("【今日のごはんチャレンジ】", 4, 4)
            num= (random.randint(0, 100) + correction_val) % len(self.challengedict)
            self.jpfontObj.printString(self.challengedict[num]["方法"], 4, 20)            

            for i in range(freq):
                menu=self.get_menu(correction_val,selected_menues)
                selected_menues.append(menu)
                
                text="{0}){1}".format(self.challengedict[num]["選択肢"][i],menu)
                self.jpfontObj.printString(text, 4, 60 + i*20)
            

        elif freq==3:
            self.jpfontObj.printString("【今日のごはんチャレンジ】", 4, 4)
            self.jpfontObj.printString("ダイスで決めようぜ!", 4, 20)
            self.jpfontObj.printString("＊ 選択肢 ＊", 4, 40)

            for i in range(freq):
                menu=self.get_menu(correction_val,selected_menues)
                selected_menues.append(menu)
                text="{0}){1}".format(options[i],menu)
                self.jpfontObj.printString(text, 4, 60 + i*20)

        gc.collect()

    def get_menu(self,correction_val,selected_menues):
        num= (random.randint(0, 100) + correction_val) % len(self.menulist)
        menu=self.menulist[num]

        if menu not in selected_menues:
            return menu
        else:
            #重複している場合はやり直し
            return self.get_menu(correction_val,selected_menues)

    def get_correction_val(self):
        #defaultの乱数に対し、加速度センサの値から補正値を生成して加算する
        ax, ay, az = self.sensor.acceleration
        correction_val= abs(math.floor(ax*100)) + abs(math.floor(ay*100)) + abs(math.floor(az*100))
        return correction_val

