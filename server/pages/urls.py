from django.urls import path

from pages.views import IndexView, ProblemView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('/problem', ProblemView.as_view(), name='problem'),
]
