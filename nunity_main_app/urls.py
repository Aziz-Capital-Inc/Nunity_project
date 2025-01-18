from django.urls import path
from nunity_main_app.views import main_home_page

urlpatterns = [
    path('', main_home_page, name='home'),
]