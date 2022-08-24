from django.urls import path
from . import views
app_name="Home"
urlpatterns=[
    path("",views.Home,name="home"),
    path("class",views.HomeClass.as_view(),name="class"),
    path("test",views.test,name="test")
]