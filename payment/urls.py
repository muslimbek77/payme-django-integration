from django.urls import path

from .views import PaymeCallBackAPIView

urlpatterns = [
  path("", PaymeCallBackAPIView.as_view()),
]