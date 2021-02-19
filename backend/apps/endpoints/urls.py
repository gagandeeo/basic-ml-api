from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MLRequestViewSet, PredictView

router = DefaultRouter(trailing_slash=False)
router.register("mlrequests", MLRequestViewSet, basename="mlrequests")
urlpatterns = [
    path('', include(router.urls)),
    path('predict/', PredictView.as_view(), name='predict')
]
