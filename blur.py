# OpenCV でカメラ映像を取得し、ぼかして表示する
# 起動時の引数　--radius でぼかしの強さを調整可能
# Qキーを入力すると終了する

import cv2
import argparse

# コマンドライン引数の処理
parser = argparse.ArgumentParser()
parser.add_argument("--radius", help="blur radius", type=int, default=5)
args = parser.parse_args()

# カメラのキャプチャを開始
cap = cv2.VideoCapture(0)

while True:
    # 画像を取得
    _, frame = cap.read()

    # ぼかし処理
    frame = cv2.blur(frame, (args.radius, args.radius))

    # 左右反転
    frame = cv2.flip(frame, 1)

    # 画像を表示
    cv2.imshow('OpenCV Web Camera', frame)

    # キー入力を待機
    key = cv2.waitKey(1) & 0xFF

    # qが押された場合は終了する
    if key == ord('q'):
        break
    
# キャプチャの後始末と，ウィンドウをすべて消す
cap.release()
cv2.destroyAllWindows()
