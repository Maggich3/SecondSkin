# from django.contrib import admin
# from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
# from main import views

# app_name = 'main'

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.popular_list, name='home'),
#     path('<slug:slug>/', views.product_detail, name='detail'),  # ← вот правильно
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# SecondSkin/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # ← Подключаем маршруты main
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
