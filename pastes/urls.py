from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:slug_key>', views.paste_detail, name="pastedetail"),
    path('<str:slug_key>/raw/', views.raw_paste, name="paste_raw_view"),
    path('history/', views.paste_history, name="pastehistory"),
]
