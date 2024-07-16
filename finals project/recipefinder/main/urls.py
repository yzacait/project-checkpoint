# main/urls.py
from django.urls import path, include
from . import views
# from .views import signup_view

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('signup/', signup_view, name='signup'),
    path('', views.home, name='home'),
    path('checklist/', views.checklist, name='checklist'),
    path('results/', views.results, name='results'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]

