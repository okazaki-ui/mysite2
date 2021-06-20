import numpy as np
from keras.models import Sequential, model_from_json
#from keras.utils import np_utils, to_categorical
from keras.preprocessing.image import load_img, save_img, img_to_array
import os
import io
import base64

def detect(upload_image): 
    img_width = 32 # 入力画像の幅
    img_height = 32 # 入力画像の高さ
    #img_ch = 3 # 3ch画像（RGB）で学習

    # 入力データ数
    #num_data = 1

    # データ格納用のディレクトリパス
    SAVE_DATA_DIR_PATH = "website/AI_model/"

    # ラベル
    labels =['飛行機', '自動車', '鳥', '猫', '鹿', '犬', '蛙', '馬', '船', 'トラック']

    # 保存したモデル構造の読み込み
    model = model_from_json(open(SAVE_DATA_DIR_PATH + "model.json", 'r').read())

    # 保存した学習済みの重みを読み込み
    model.load_weights(SAVE_DATA_DIR_PATH + "weight.hdf5")

    # 画像の読み込み（32×32にリサイズ）
    # 正規化, 4次元配列に変換（モデルの入力が4次元なので合わせる）
    #img = load_img(SAVE_DATA_DIR_PATH + "test.png", target_size=(img_width, img_height))
    img = load_img(upload_image, target_size=(img_width, img_height))
    img = img_to_array(img) 
    img = img.astype('float32')/255.0
    img = np.array([img])

    # 分類機に入力データを与えて予測（出力：各クラスの予想確率）
    y_pred = model.predict(img)

    # 最も確率の高い要素番号（=予想する数字）
    number_pred = np.argmax(y_pred) 

    # 予測結果の表示
    print("y_pred:", y_pred)  # 出力値
    print("number_pred:", number_pred)  # 最も確率の高い要素番号
    print('label_pred：', labels[int(number_pred)]) # 予想ラベル（最も確率の高い要素）

    result_list=labels[int(number_pred)]
    result_name=labels[int(number_pred)]
    result_img=upload_image

    #画像の保存(パターン1)
    saveimg = load_img(upload_image)
    #save_img(os.getcwd() + "\website\static\img\dest2.jpg", saveimg)
    buffer  = io.BytesIO()
    saveimg.save(buffer, format="PNG") #ここで書き出し   
    base64Img = base64.b64encode(buffer.getvalue()).decode().replace("'", "")
    result_img = base64Img

    #return (result_list, result_name)
    return (result_list, result_name, result_img)
