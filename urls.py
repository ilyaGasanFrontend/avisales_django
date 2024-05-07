
from django.contrib import admin
from django.urls import path, include
from bookings.views import add_flight  # Импорт представления для страницы добавления рейса

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', add_flight, name='add_flight'),  # URL-шаблон для корневой страницы
    path('bookings/', include('bookings.urls')),
]