from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogHandler,name="Allblogs"),
    path('<int:blog_id>/',views.detailblogs,name="detailblogs"),
]
