from django.urls import path
from . import views as v

urlpatterns = [
    path('register/', v.register_view, name="register" )
]