from jaiib import views
from django.urls import path
from .views import checkbrain, AjaxHandler
from user.models import brainjaiib


urlpatterns = [
    path("chkbrn/",views.checkbrain,name = "checkbrain"),
    path("solomon/", AjaxHandler.as_view()),
    path("questionfetch/", views.fetchquestion, name="fetchquestion"),
]
