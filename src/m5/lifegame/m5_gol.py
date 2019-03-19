from m5stack import *
from game_of_life import GameOfLife


class App:
    def __init__(self):
        try:
            self.cnt=0
            self.gol_obj=GameOfLife()
            lcd.clear()
            lcd.setColor(lcd.WHITE)

            buttonA.wasPressed(self.on_AwasPressed)

            while True:
                self.print_gol()
                
        except Exception as e:
            lcd.print(str(e))


    def on_AwasPressed(self): 
        lcd.clear()
        self.gol_obj.reset()
        

    def print_gol(self):
        #次世代セルを計算
        matrix=self.gol_obj.calc_state()
        
        #表示情報の取得( 1を黒, 0を白で表示)
        img=self.gol_obj.create_matrix_img(matrix)

        # 表示をアップデート
        self.draw_pyxel_matrix(img)
        self.cnt+=1
        #lcd.print(str(self.cnt))
        

    def draw_pyxel_matrix(self,img):

        for y, values in enumerate(img):
            for x, val in enumerate(values):
                if val==255:
                    #lcd.rect(x*15+45 ,y*15+5, 15 ,15, lcd.BLACK,lcd.BLACK)
                    lcd.circle(x*15+55 ,y*15+15, 7 , lcd.BLACK,lcd.BLACK)

                elif val==0:
                    #lcd.rect(x*15+45 ,y*15+5, 15 ,15, lcd.WHITE,lcd.WHITE)
                    lcd.circle(x*15+55 ,y*15+15, 7, lcd.WHITE,lcd.WHITE)

        


