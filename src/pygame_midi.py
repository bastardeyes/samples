"""
ドから半音ずつ音が上がって、欽ちゃんの仮装大賞っぽい音がでます
"""
import pygame
import pygame.midi

import sys
from time import sleep
from pygame.locals import QUIT

class MIDI_PLAYER:

    def __init__(self):
        pygame.init()
        pygame.midi.init()
        port = pygame.midi.get_default_output_id() #usb
        print(port)
        self.midi_out=pygame.midi.Output(port)
        self.midi_out.set_instrument(0)

    def note_onoff(self,pitch=60,velocity=80,onoff="on"):
        midi_out=self.midi_out
        if onoff=="on":
            midi_out.note_on(pitch, velocity)
        else:
            midi_out.note_off(pitch, velocity)

    def exit(self):
        QUIT()

   
def pray_mp():
    
    try:        
        mp = MIDI_PLAYER()
        
        pitch=60 #ドの音
        velocity=80 #音の立ち上がり
        for i in range(0,12):
            mp.note_onoff(pitch,velocity,"on") #note_onで音を出す。note_offになるまで伸ばす
            sleep(.500)
            mp.note_onoff(pitch,velocity,"off")
            pitch +=1

        mp.quit()

    except Exception as e:
        print(e)

if __name__=='__main__':
    pray_mp()
