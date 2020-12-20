from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('translate/', views.translate),
    path('text_recognition/', views.text_recognition),
    path('summary/', views.summary),
    path('summary_web/', views.summary_web),
    path('summary_text/', views.summary_text),
    path('word_tokenize/', views.word_tokennize),
    path('help/', views.help),
    path('translate2/', views.translate2),
    path('sentiment_analysis/', views.sent_analysis),


]