from django.urls import path, include

from .views import loginView

app_name= "loginPage"
urlpatterns = [
    path("hey/", loginView, name="loginView")

]