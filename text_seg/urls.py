from django.urls import path

from . import views

urlpatterns = [
    path('task/text_seg/run', views.tokenize, name="text_seg"),
    path('task/part_of_speech/run', views.part_of_speech, name="part_of_speech")
]