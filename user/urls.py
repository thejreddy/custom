from user import views
from django.urls import path
from .views import correctanswer,jaffa


urlpatterns = [
    path("success/",views.correctanswer, name="success"),
    path("updatescore/",views.jaffa, name="jaffa"),
]
