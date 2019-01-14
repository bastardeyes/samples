# 自分用備忘録

# 大まかな環境構築手順メモ
1.USBドライバーをインストール
https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

2.ESP32のインストール(FW書き込みに必要)
https://github.com/espressif/arduino-esp32/blob/master/docs/arduino-ide/mac.md

3.オフラインファームのインストール
4.ampyのインストール(m5stack内のファイル書き込みに必要)
https://qiita.com/cyubachi/items/ba54e1122450e790013a


※ 2019.1月時点で、M5Croudからソースを開くことができなかったため、オフライン利用している。無理してオンラインで使わなくてもいいっぽい。
※ M5Croudをオンライン利用する場合、Wi-FiのSSID/PW設定が必要だが、SSIDがステルスだと扱えない。

※ ArduinoIDEは、MicroPythonでは不要。
Cのサンプルを確認するのであれば、下記のサイトがおすすめ。
https://qiita.com/hmmrjn/items/2b2da09eecffcbdbad85


#実行手順メモ
export AMPY_PORT=/dev/tty.SLAB_USBtoUART
ampy put ./main.py /flash/main.py
ampy run ./main.py