import time
from machine import UART

class Tenorion:
    def __init__(self):
        self.uart = UART(2, tx=17, rx=16)
        self.uart.init(31250, bits=8, parity=None, stop=1)#MIDI

    def remote_on(self,is_intialize=True,is_play=True):
        midi_list= bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0xF7])
        if is_intialize!=True:
            midi_list=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0xF7])

        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20) 
        return midi_list


    def remote_off(self,is_play=True):
        midi_list= bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20) 
        return midi_list

    def play(self,is_play=True):
        midi_list=bytes( [0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x08, 0x01, 0x00, 0x00, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20) 
        return midi_list

    def pause(self,is_play=True):
        midi_list=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20) 
        return midi_list

    def clear_all_layer(self,layer=0x11,is_play=True):
        block=0x00
        #layer=0x11
        midi_list=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x0A, block, layer, 0x00, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20) 
        return midi_list

    def clear_all_block(self,block=0x0A,is_play=True):
        block=0x0A
        layer=0x0A
        midi_list=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x0A, block, layer, 0x01, 0x01, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20)
        return midi_list

    def clear_all_block_and_layer(self,is_play=True):
        block=0x0A
        layer=0x0A
        midi_list=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x0A, block, layer, 0x00, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20)
        return midi_list

    def change_loop_indicator_position(self,play_point=0x11,is_play=True):
        midi_list=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x09, play_point, 0x00, 0x00, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20)
        return midi_list

    def led_on_off(self,on_off=False,x=0x00,y=0x00,layer=0x00,is_play=True):
        led_mode=0x04 #off
        if on_off==True:
            led_mode=0x02 #on
        midi_list=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, led_mode, x, y, layer, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20)
        return midi_list

    def led_hold_on(self,x=0x00,y=0x00,layer=0x00,is_play=True):
        mode=0x00
        midi_list=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x06, 0x00, 0x00, 0x02, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20)
        return midi_list

    # score_mode or random_mode
    def led_hold_on_off(self,on_off=False,x=0x00,y=0x00,layer=0x00,is_play=True):
        led_mode=0x01 #off
        if on_off==True:
            led_mode=0x00 #on
        midi_list= bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x06, x, y, layer, led_mode, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20)
        return midi_list

    def current_block_change(self,block=0x00,is_play=True):
         # block = 0 to 15
        midi_list= bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x0F, block, 0x00, 0x00, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20)
        return midi_list
       
    def current_layer_change(self,layer=0x00,is_play=True):
        midi_list=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x10, layer, 0x00, 0x00, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20)
        return midi_list
        """
        layer = 0 to 15
        00-06 )Score mode
        07-10 )Random mode
        11-12 )Draw mode
        13    )Bounce mode
        14    )Push mode
        15    )Solo mode
        """
        

    def layer_parameter_change(self,param_id,d1,d2,layer=0x00,is_play=True):   
        midi_list=bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x0D, param_id, d1, d2, layer, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20)
        return midi_list
        """
        param_id | range
        0 instrument = 0 to 255
        1 sound_length = 1 to 999
        2 loop_speed = 1 to 4
        3 loop_point(top & end) =[d1]0 to 15 & [d2]0 to 15
        4 volume = 0 to 127
        5 panpot = 0 to 127
        6 animation_type = 0 to 5
          => 0=simple, 1=circle, 2= square, 3=Diamond, 4=Cross ,5=Plus
        7 animation_size = 1 to 22
        8 animation_direction(縮小/拡大) = 0 to 1
          => 0=shrink, 1= expand
        9 octave = 59 -(64)-69  *64が基準ド

        *d1は上位7bit,d2は下位7bit。(range参照)
        """

    
    def common_param_change(self,param_id,d1,d2,is_play=True):
        midi_list= bytes([0xF0, 0x43, 0X73, 0x01, 0x33, 0x01, 0x00, 0x0C, param_id, d1, d2, 0x00, 0x00, 0xF7])
        if is_play==True:
            self.uart.write(midi_list)
            time.sleep_ms(20)
        return midi_list
        """
        param_id | range
        0 mastar_volume = 0 to 127
        1 master_tempo = 40 to 240
        2 master_scale = 0 to 9
         => 0=ionian, 1=Dorian, 2=Phrygian, 3=Lydian, 4=Mixolydian, 5=Aelian, 6=Locrian, 7=Chromatic, 8=OKINAWA ,9=user
        3 master_transpose = 57 -(64)-72
        4 master_loop_speed = 1 to 4
        5 master_loop_point_top = 0 to 15
        6 master_loop_point_end = 0 to 15
        7 reset_loop_timing = (don't care)
        8 mute = 0 to 1
         => 0=on, 1=off
        9 swing_rate = 0-(23)-46
        10 reverb_type = 0 to 9
         => 0=no effect, 1=hall, 2=hall2, 3=room1, 4=room2, 5=room3, 6=stage1, 7=stage2, 8=plate1, 9=plate2
        11 chorus_type = 0 to 4
         => 0=no eddect, 1=chorus1 ,2=chorus2, 3=flanger1, 4=flanger2
        12 chorus_param = 0 to 127

        """

    def execute_midi_lists(self,midi_lists):
        for x in midi_lists:
            self.uart.write(x)
            time.sleep_ms(20)
    


