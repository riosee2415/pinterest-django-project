from django.urls import path
from django.views.generic import TemplateView
from articleapp.views import (
    AritcleCreateView,
    ArticleDetailView,
    AritcleUpdateView,
    ArticleDeleteView,
    ArticleListView,
)

app_name = "articleapp"

urlpatterns = [
    path("list/", ArticleListView.as_view(), name="list"),
    path("create/", AritcleCreateView.as_view(), name="create"),
    path("detail/<int:pk>", ArticleDetailView.as_view(), name="detail"),
    path("update/<int:pk>", AritcleUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", ArticleDeleteView.as_view(), name="delete"),
]
