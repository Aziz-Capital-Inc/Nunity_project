from django.urls import path
from nunity_main_app.views import view_form

urlpatterns = [
    path('', view_form, name='home'),
]