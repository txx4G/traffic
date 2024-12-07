from django.urls import path

from pages.views import IndexView, ProblemView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('problem/<str:coords>/', ProblemView.as_view(), name='problem'),
]
