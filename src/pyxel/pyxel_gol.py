import pyxel
from lib.game_of_life import GameOfLife


gol=GameOfLife()

class App:
    def __init__(self):
        pyxel.init(170,170)
        pyxel.mouse(False)

        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        elif pyxel.btnp(pyxel.KEY_R):
            gol.reset()

    def draw(self):
        pyxel.cls(0)

        #次世代セルを計算
        matrix=gol.calc_state()
        
        #表示情報の取得( 1を黒, 0を白で表示)
        img=gol.create_matrix_img(matrix)

        # 表示をアップデート
        self.draw_pyxel_matrix(img)

    def draw_pyxel_matrix(self,img):
        for y, values in enumerate(img):
            for x, val in enumerate(values):
                if val==255:
                    pyxel.rect(x*10+10 ,y*10+10,x*10+10+10 ,y*10+10+10,col=0)

                elif val==0:
                    pyxel.rect(x*10+10 ,y*10+10,x*10+10+10 ,y*10+10+10,col=7)


if __name__=='__main__':
    App()