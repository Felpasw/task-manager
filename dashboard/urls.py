from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update-task/', views.update_task, name='update_task'),
    path('create-task/', views.create_task, name='create_task'),
    path('delete-task/', views.delete_task, name='delete_task'),
    path('logout',views.logoutUser, name='logout'),
    #path('login/', views.login, name='login'),
    path('add_user/', views.add_user, name='add_user')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)