from django.urls import path
from . import views
app_name="Home"
urlpatterns=[
    path("",views.Home,name="home"),
    path("class",views.HomeClass.as_view(),name="class"),
    path("test",views.test,name="test"),
    path("coin",views.GetCriptoPrice.as_view(),name="coin"),
    path("article/",views.ArticleView.as_view()),
    path("article/<int:pk>",views.ArticleDetail.as_view()),
    path("article/add",views.AddArticle.as_view())
]