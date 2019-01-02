"""
下記、MITライセンスのコードを再利用しております。
https://github.com/alifelab/alife_book_src

"""

import numpy as np

HEIGHT=15
WIDTH=15

class GameOfLife:
    def __init__(self, value_range_min=0, value_range_max=1):
        self.next_state = np.empty((HEIGHT,WIDTH), dtype=np.int8)

        # 初期データの設定
        self.state = np.random.randint(2, size=(HEIGHT,WIDTH), dtype=np.int8)
        self.value_range = (value_range_min, value_range_max)


    def calc_state(self):
        for i in range(HEIGHT):
            for j in range(WIDTH):
                # 自分と近傍のセルの状態を取得
                # c: center (自分自身)
                # nw: north west, ne: north east, c: center ...
                nw = self.state[i-1,j-1]
                n  = self.state[i-1,j]
                ne = self.state[i-1,(j+1)%WIDTH]
                w  = self.state[i,j-1]
                c  = self.state[i,j]
                e  = self.state[i,(j+1)%WIDTH]
                sw = self.state[(i+1)%HEIGHT,j-1]
                s  = self.state[(i+1)%HEIGHT,j]
                se = self.state[(i+1)%HEIGHT,(j+1)%WIDTH]
                neighbor_cell_sum = nw + n + ne + w + e + sw + s + se
                if c == 0 and neighbor_cell_sum == 3:
                    self.next_state[i,j] = 1
                elif c == 1 and neighbor_cell_sum in (2,3):
                    self.next_state[i,j] = 1
                else:
                    self.next_state[i,j] = 0
        
        self.state, self.next_state = self.next_state, self.state

        matrix = 1-self.state
        return matrix
    
    def create_matrix_img(self,matrix): 
        matrix[matrix < self.value_range[0]] = self.value_range[0]
        matrix[matrix > self.value_range[1]] = self.value_range[1]
        img = ((matrix.astype(np.float64) - self.value_range[0]) / (self.value_range[1] - self.value_range[0]) * 255).astype(np.uint8)

        return img


    def reset(self):
        self.state=np.random.randint(2, size=(HEIGHT,WIDTH), dtype=np.int8)

        