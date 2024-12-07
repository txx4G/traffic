from django.urls import path

from map_traffic.views import SaveClaimView

urlpatterns = [
    path('save_claim', SaveClaimView.as_view(), name='save_claim'),
]
