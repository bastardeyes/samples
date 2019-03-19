"""
下記、MITライセンスのコードを再利用しております。
https://github.com/alifelab/alife_book_src
=>MycroPythonはnumpyが利用できなかったので、書き換えています。
"""

import random

class GameOfLife:
    def __init__(self, value_range_min=0, value_range_max=1):
        self.HEIGHT=15
        self.WIDTH=15

        self.next_state = [[random.randint(-128, 127) for i in range(self.HEIGHT)] for j in range(self.WIDTH)]

        # 初期データの設定
        self.state =  [[random.randint(0, 1) for i in range(self.HEIGHT)] for j in range(self.WIDTH)]
        self.value_range = (value_range_min, value_range_max)


    def calc_state(self):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                # 自分と近傍のセルの状態を取得
                # c: center (自分自身)
                # nw: north west, ne: north east, c: center ...
                nw = self.state[i-1][j-1]
                n  = self.state[i-1][j]
                ne = self.state[i-1][(j+1)%self.WIDTH]
                w  = self.state[i][j-1]
                c  = self.state[i][j]
                e  = self.state[i][(j+1)%self.WIDTH]
                sw = self.state[(i+1)%self.HEIGHT][j-1]
                s  = self.state[(i+1)%self.HEIGHT][j]
                se = self.state[(i+1)%self.HEIGHT][(j+1)%self.WIDTH]
                neighbor_cell_sum = nw + n + ne + w + e + sw + s + se
                if c == 0 and neighbor_cell_sum == 3:
                    self.next_state[i][j] = 1
                elif c == 1 and neighbor_cell_sum in (2,3):
                    self.next_state[i][j] = 1
                else:
                    self.next_state[i][j] = 0
        
        self.state, self.next_state = self.next_state, self.state

        matrix = [[ 1- self.state[i][j] for i in range(self.HEIGHT)] for j in range(self.WIDTH)]
        return matrix
    
    def create_matrix_img(self,matrix):
        img=[[None for i in range(self.HEIGHT)] for j in range(self.WIDTH)]

        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):

                val=matrix[i][j]

                if matrix[i][j]<self.value_range[0]:
                    val=self.value_range[0]
                elif matrix[i][j]>self.value_range[1]:
                    val=self.value_range[1]
                
                img[i][j]=abs(int( ((float(val)-self.value_range[0] )/ (self.value_range[1] - self.value_range[0]) * 255)))
        return img


    def reset(self):
        self.next_state = [[random.randint(-128, 127) for i in range(self.HEIGHT)] for j in range(self.WIDTH)]
        self.state =  [[random.randint(0, 1) for i in range(self.HEIGHT)] for j in range(self.WIDTH)]

