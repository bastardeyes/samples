"""
nochi様よりサンプル拝借いたしました。多謝。
(元々はSD読み込みです)
http://shikarunochi.matrix.jp/?p=2260
"""

from m5stack import lcd

class jpfont:

    def __init__(self):
        self.fontFile = open("/flash/assets/fontData.bin", "rb")
        self.fontCodeFile = open("/flash/assets/fontCode.bin", "rb")#Unicodeコード→フォント並び順変換
        self.fontDataCache = {} #フォントデータキャッシュ
        self.zenkaku="ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［￥］＾＿‘｛｜｝～　０１２３４５６７８９"
        self.hankaku="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 0123456789"
 
    def __del__(self):
        self.fontfile.close()
        self.fontCodeFile.close()

    def printChar(self, char, base_x, base_y):
        if self.hankaku.find(char) != -1:
            char=self.zenkaku[self.hankaku.find(char)]

        fontData = None
        if char in self.fontDataCache:#キャッシュにあったらそれ使う
            fontData = self.fontDataCache[char]
        else:
            if ord(char) < 65536:
                #フォントの位置取得
                self.fontCodeFile.seek((ord(char)-1) * 2)
                fontIndex = int.from_bytes(self.fontCodeFile.read(2), "big")
                #フォントデータ取得
                self.fontFile.seek(fontIndex * 26)
                fontData = self.fontFile.read(26)
                if len(self.fontDataCache) < 100:
                    self.fontDataCache[char] = fontData #フォントキャッシュ100個までにしておく
        
        if fontData is not None:
            y = 0
            index = 0
            for fontDataByte in fontData:
                if index % 2 == 0:
                    fontData_line = fontDataByte << 8
                    index = index + 1
                    continue
                else:
                    fontData_line = fontData_line + fontDataByte
                
                for x in range(15):
                    if fontData_line >> (15 - x) & 1 == 1: #ビット上側から、1か0かチェック
                        lcd.rect((x + base_x )*2 , (y + base_y) * 2 , 2, 2) #１ならその位置にドット打つ
                index = index + 1
                y = y + 1

    def printString(self, string, base_x, base_y):
        offset = base_x
        for c in string:
            self.printChar(c ,offset, base_y) #1文字ずつ描画呼び出し
            offset = offset + 12


