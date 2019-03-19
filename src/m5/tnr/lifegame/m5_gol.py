from m5stack import *
from game_of_life import GameOfLife
from m5_tnr import Tenorion

class App:
    def __init__(self):
        try:
            self.tnr = Tenorion() # tenorion initialize
            self.init_tenorion()
            self.tnr.play()
            
            
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
        

    def draw_pyxel_matrix(self,img):
        tnr=self.tnr
        layer=4
        midi_lists=[]

        scale=0 
        #if img.sum()>0:
        #    scale= int(img.sum()/255%7)

        tnr.common_param_change(2,0,scale) #scale変更
        tnr.current_layer_change(layer=layer)

        for y, values in enumerate(img):
            for x, val in enumerate(values):
                if val==255:
                    #lcd.rect(x*15+45 ,y*15+5, 15 ,15, lcd.BLACK,lcd.BLACK)
                    lcd.circle(x*15+55 ,y*15+15, 7 , lcd.BLACK,lcd.BLACK)
                    midi_lists.append(tnr.led_hold_on_off(on_off=False,x=x,y=y,layer=layer,is_play=False))  
                    

                elif val==0:
                    #lcd.rect(x*15+45 ,y*15+5, 15 ,15, lcd.WHITE,lcd.WHITE)
                    lcd.circle(x*15+55 ,y*15+15, 7, lcd.WHITE,lcd.WHITE)
                    midi_lists.append(tnr.led_hold_on_off(on_off=True,x=x,y=y,layer=layer,is_play=False))  

        tnr.current_layer_change(layer=layer)
        tnr.execute_midi_lists(midi_lists)              
    
    def init_tenorion(self):
        tnr=self.tnr
        tnr.remote_on(is_intialize=True)   
        tnr.clear_all_block_and_layer()
        tnr.current_block_change(0)
        tnr.current_layer_change(0)
        
        for layer in range(6):
            tnr.layer_parameter_change(2,0,3,layer) #speed
            tnr.layer_parameter_change(6,0,0,layer) #animation_type
            tnr.layer_parameter_change(7,0,1,layer) #animation_size
            tnr.layer_parameter_change(8,0,0,layer) #animation_direction   
           

        tnr.common_param_change(2,0,0) #scale
        tnr.common_param_change(4,0,2) #scroll speed
        tnr.common_param_change(7,0,0) #loop_timing
        tnr.common_param_change(3,0,64)#key default


    def reset_tenorion(self):
        tnr=self.tnr
        tnr.clear_all_block()
        tnr.pause()
        tnr.clear_all_block_and_layer()
    





        


