from django.urls import path

from pages.views import IndexView, ProblemView, ClaimView, EffectiveView, PredictView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('problem/<int:problem_id>/', ProblemView.as_view(), name='problem'),
    path('claim/', ClaimView.as_view(), name='claim'),
    path('predict/', PredictView.as_view(), name='predict'),
    path('effective/', EffectiveView.as_view(), name='effective'),
]
