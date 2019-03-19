from m5stack import *
from m5_gol import App

try:
    obj=App()

except Exception as e:
    lcd.print(str(e))