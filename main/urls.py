from django.urls import path
from main.views import (
    show_main, create_news, show_news,
    show_xml, show_json, show_xml_by_id, show_json_by_id,
    register, login_user, logout_user, choose_role
)

app_name = 'main'

urlpatterns = [
    # 🔥 HALAMAN AWAL (WAJIB KE SINI)
    path('', choose_role, name='choose_role'),

    # 🔐 AUTH
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),

    # 🧠 DASHBOARD (HARUS LOGIN)
    path('dashboard/', show_main, name='show_main'),

    # 📰 NEWS
    path('create-news/', create_news, name='create_news'),
    path('news/<str:id>/', show_news, name='show_news'),

    # 📦 API
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
]