from django.urls import path
from .views import PredView

'''
urlpatterns = [
    path('', views.IndexView),
    #path('about/', IndexView.as_view()),
]
'''

urlpatterns = [
    path('', PredView.as_view(), name='index'),
]
