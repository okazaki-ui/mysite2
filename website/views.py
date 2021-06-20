'''
from django.shortcuts import render
from django.views.generic import TemplateView

#メイン関数
def IndexView(request):
   my_dict = {'callme' : "Hello you called me from views.index!" }
   return render(request,'index.html',context=my_dict)
'''


from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ImageForm
from .main import detect
from .models import Images
from keras.preprocessing.image import load_img,save_img
import cloudinary
import cloudinary.uploader
import cloudinary.api

class PredView(TemplateView):
    # コンストラクタ
    def __init__(self):
        self.params = {'result_list': [],
                       'result_name': "",
                       'result_img': "",
                       'form': ImageForm()
                       }

    
    # GETリクエスト（index.htmlを初期表示）
    #クラス関数を読んだときに自動で呼び出される
    def get(self, req):
        return render(req, 'index.html', self.params)
    
    # POSTリクエスト（index.htmlに結果を表示）
    def post(self, req):
        # POSTされたフォームデータを取得
        form = ImageForm(req.POST, req.FILES)
        # フォームデータのエラーチェック
        if not form.is_valid():
            raise ValueError('invalid form')
        # フォームデータから画像ファイルを取得
        image = form.cleaned_data['image']
        # 画像ファイルを指定して顔分類
        
        result = detect(image)
        # 顔分類の結果を格納
        self.params['result_list'], self.params['result_name'], self.params['result_img'] = result

        return render(req, 'index.html', self.params)
    
