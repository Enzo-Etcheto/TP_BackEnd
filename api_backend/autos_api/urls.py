from django.urls import path
from autos_api import views

urlpatterns = [
path('index_auto', views.index_auto, name='index_auto'),
path('index_user', views.index_user, name='index_user'),
path('auto_rest/',views.auto_rest, name='auto_rest'),
path('user_rest/',views.users_rest, name='user_rest'),
path('new_auto/',views.NewAutoView.as_view(), name='new_auto'),
path('new_user/',views.NewUserView.as_view(), name='new_user'),
]